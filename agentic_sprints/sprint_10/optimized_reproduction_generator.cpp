#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <system_error>
#include <vector>

using Int = __int128_t;
using Matrix = std::vector<std::vector<int>>;
using Vec = std::vector<int>;

struct Args {
    int order = 13;
    long long threshold_normalized = 2173;
    long long max_nodes = 200000;
    int max_depth = 0;
    long long progress_every = 25000;
    long long lex_permutation_cap = 2000000;
    std::string phi_mode = "congruent";
    std::string bound_mode = "km";
    std::string emax_mode = "dynamic";
    std::string lexmax_mode = "always";
    bool skip_lexmax = false;
    bool skip_block_order = false;
    int shard_count = 1;
    int shard_index = 0;
    int shard_depth = 0;
    std::string output_dir = "outputs/smoke";
};

struct LevelStats {
    long long tested = 0;
    long long accepted = 0;
    long long pruned_structure = 0;
    long long pruned_row_order = 0;
    long long pruned_block_order = 0;
    long long pruned_pd = 0;
    long long pruned_bound = 0;
    long long pruned_lexmax = 0;
    long long full_square_candidates = 0;
    long long full_below_threshold = 0;
    long long full_not_square = 0;
};

struct Blocks {
    std::vector<std::pair<int, int>> intervals;
    bool contiguous = true;
};

struct State {
    Args args;
    std::vector<int> phi;
    int minimal = 1;
    Int threshold_det = 0;
    std::vector<Int> pow_order_minus_one;
    std::vector<LevelStats> levels;
    long long nodes_tested = 0;
    long long recursion_calls = 0;
    long long candidates_written = 0;
    long long shard_skipped = 0;
    long long gamma_tests = 0;
    long long lexmax_checks = 0;
    long long lexmax_inconclusive = 0;
    long long lexmax_permutations_seen = 0;
    int max_depth_seen = 1;
    bool stopped_by_cap = false;
    std::chrono::steady_clock::time_point start;
    std::ofstream candidate_out;
};

std::string int_to_string(Int value) {
    if (value == 0) return "0";
    bool negative = value < 0;
    if (negative) value = -value;
    std::string out;
    while (value > 0) {
        int digit = static_cast<int>(value % 10);
        out.push_back(static_cast<char>('0' + digit));
        value /= 10;
    }
    if (negative) out.push_back('-');
    std::reverse(out.begin(), out.end());
    return out;
}

Int det_bareiss(const Matrix& matrix) {
    int n = static_cast<int>(matrix.size());
    if (n == 0) return 1;
    std::vector<std::vector<Int>> a(n, std::vector<Int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) a[i][j] = matrix[i][j];
    }
    Int sign = 1;
    Int previous = 1;
    for (int k = 0; k < n - 1; ++k) {
        int pivot = k;
        while (pivot < n && a[pivot][k] == 0) ++pivot;
        if (pivot == n) return 0;
        if (pivot != k) {
            std::swap(a[k], a[pivot]);
            sign = -sign;
        }
        Int pivot_value = a[k][k];
        for (int i = k + 1; i < n; ++i) {
            for (int j = k + 1; j < n; ++j) {
                a[i][j] = (a[i][j] * pivot_value - a[i][k] * a[k][j]) / previous;
            }
        }
        previous = pivot_value;
        for (int i = k + 1; i < n; ++i) a[i][k] = 0;
        for (int j = k + 1; j < n; ++j) a[k][j] = 0;
    }
    return sign * a[n - 1][n - 1];
}

int positive_mod(int value, int modulus) {
    int out = value % modulus;
    return out < 0 ? out + modulus : out;
}

std::vector<int> phi_orrick_restricted(int order) {
    std::vector<int> phi;
    if (order % 4 == 1) {
        for (int value = 1; value >= 2 - order; value -= 4) phi.push_back(value);
    } else if (order % 4 == 3) {
        for (int value = -1; value <= order - 2; value += 4) phi.push_back(value);
    } else {
        for (int value = 0; value < order; value += 2) {
            int positive = value;
            int negative = -value;
            if (positive_mod(positive - order, 4) == 0 && positive != order) phi.push_back(positive);
            if (negative != positive && positive_mod(negative - order, 4) == 0 && -negative != order) phi.push_back(negative);
        }
        std::sort(phi.begin(), phi.end(), [](int left, int right) {
            return std::abs(left) < std::abs(right);
        });
    }
    return phi;
}

std::vector<int> phi_congruent_ordered_by_abs(int order) {
    std::vector<int> phi;
    for (int value = 1 - order; value < order; ++value) {
        if (positive_mod(value - order, 4) == 0) phi.push_back(value);
    }
    std::sort(phi.begin(), phi.end(), [](int left, int right) {
        int left_abs = std::abs(left);
        int right_abs = std::abs(right);
        if (left_abs != right_abs) return left_abs < right_abs;
        return left < right;
    });
    return phi;
}

std::vector<int> make_phi(int order, const std::string& mode) {
    if (mode == "restricted") return phi_orrick_restricted(order);
    if (mode == "congruent") return phi_congruent_ordered_by_abs(order);
    std::cerr << "Unknown phi mode: " << mode << "\n";
    std::exit(2);
}

std::vector<int> allowed_values(const std::vector<int>& phi, int max_abs) {
    std::vector<int> values;
    for (int value : phi) {
        if (std::abs(value) <= max_abs) values.push_back(value);
    }
    return values;
}

int compare_abs_values(int left, int right) {
    int left_abs = std::abs(left);
    int right_abs = std::abs(right);
    if (left_abs < right_abs) return -1;
    if (left_abs > right_abs) return 1;
    return 0;
}

int compare_vectors_abs(const Vec& left, const Vec& right) {
    int shared = std::min(left.size(), right.size());
    for (int i = 0; i < shared; ++i) {
        int comparison = compare_abs_values(left[i], right[i]);
        if (comparison != 0) return comparison;
    }
    if (left.size() < right.size()) return -1;
    if (left.size() > right.size()) return 1;
    return 0;
}

Vec partial_row(const Matrix& matrix, int row, int length) {
    Vec out;
    out.reserve(length);
    for (int column = 0; column < length; ++column) out.push_back(matrix[row][column]);
    return out;
}

int compare_matrices_abs_lex(const Matrix& left, const Matrix& right) {
    int shared = std::min(left.size(), right.size());
    for (int row = 1; row < shared; ++row) {
        Vec left_partial = partial_row(left, row, row);
        Vec right_partial = partial_row(right, row, row);
        int comparison = compare_vectors_abs(left_partial, right_partial);
        if (comparison != 0) return comparison;
    }
    if (left.size() < right.size()) return -1;
    if (left.size() > right.size()) return 1;
    return 0;
}

int compare_rows_abs_prefix(const Matrix& matrix, int earlier, int later, int length) {
    for (int column = 0; column < length; ++column) {
        int comparison = compare_abs_values(matrix[earlier][column], matrix[later][column]);
        if (comparison != 0) return comparison;
    }
    return 0;
}

bool is_row_lex_ordered(const Matrix& matrix) {
    int size = static_cast<int>(matrix.size());
    for (int earlier = 0; earlier < size - 1; ++earlier) {
        for (int later = earlier + 1; later < size; ++later) {
            if (compare_rows_abs_prefix(matrix, earlier, later, earlier + 1) <= 0) return false;
        }
    }
    return true;
}

Matrix extend_matrix(const Matrix& matrix, const Vec& vector, int order) {
    int size = static_cast<int>(matrix.size());
    Matrix candidate(size + 1, std::vector<int>(size + 1, order));
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) candidate[i][j] = matrix[i][j];
    }
    for (int i = 0; i < size; ++i) {
        candidate[i][size] = vector[i];
        candidate[size][i] = vector[i];
    }
    return candidate;
}

Matrix augment_with_gamma(const Matrix& matrix, const Vec& gamma, int c) {
    int size = static_cast<int>(matrix.size());
    Matrix augmented(size + 1, std::vector<int>(size + 1, c));
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) augmented[i][j] = matrix[i][j];
    }
    for (int i = 0; i < size; ++i) {
        augmented[i][size] = gamma[i];
        augmented[size][i] = gamma[i];
    }
    return augmented;
}

bool is_square(Int value, Int& root) {
    if (value < 0) return false;
    long double approx = std::sqrt(static_cast<long double>(value));
    Int guess = static_cast<long long>(approx);
    while ((guess + 1) * (guess + 1) <= value) ++guess;
    while (guess * guess > value) --guess;
    root = guess;
    return guess * guess == value;
}

int find_parent(std::vector<int>& parent, int item) {
    if (parent[item] == item) return item;
    parent[item] = find_parent(parent, parent[item]);
    return parent[item];
}

void union_parent(std::vector<int>& parent, int left, int right) {
    int left_root = find_parent(parent, left);
    int right_root = find_parent(parent, right);
    if (left_root != right_root) parent[right_root] = left_root;
}

Blocks compute_blocks(const Matrix& matrix, int minimal) {
    int size = static_cast<int>(matrix.size());
    std::vector<int> parent(size);
    std::iota(parent.begin(), parent.end(), 0);
    for (int i = 0; i < size; ++i) {
        for (int j = i + 1; j < size; ++j) {
            if (matrix[i][j] != minimal) union_parent(parent, i, j);
        }
    }

    std::vector<std::vector<int>> groups(size);
    for (int i = 0; i < size; ++i) groups[find_parent(parent, i)].push_back(i);

    Blocks blocks;
    for (const auto& group : groups) {
        if (group.empty()) continue;
        int start = group.front();
        int end = group.back();
        if (end - start + 1 != static_cast<int>(group.size())) blocks.contiguous = false;
        blocks.intervals.push_back({start, end});
    }
    std::sort(blocks.intervals.begin(), blocks.intervals.end());
    return blocks;
}

Matrix submatrix_interval(const Matrix& matrix, int start, int end) {
    int size = end - start + 1;
    Matrix out(size, std::vector<int>(size));
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) out[i][j] = matrix[start + i][start + j];
    }
    return out;
}

bool blocks_descending(const Matrix& matrix, const Blocks& blocks) {
    for (size_t index = 1; index < blocks.intervals.size(); ++index) {
        auto previous = blocks.intervals[index - 1];
        auto current = blocks.intervals[index];
        int previous_size = previous.second - previous.first + 1;
        int current_size = current.second - current.first + 1;
        int shared = std::min(previous_size, current_size);
        int comparison = 0;
        for (int row = 1; row < shared && comparison == 0; ++row) {
            for (int column = 0; column < row; ++column) {
                comparison = compare_abs_values(
                    matrix[previous.first + row][previous.first + column],
                    matrix[current.first + row][current.first + column]
                );
                if (comparison != 0) break;
            }
        }
        if (comparison == 0) {
            if (previous_size < current_size) comparison = -1;
            else if (previous_size > current_size) comparison = 1;
        }
        if (comparison < 0) return false;
    }
    return true;
}

bool all_minimal(const Vec& vector, int minimal) {
    return std::all_of(vector.begin(), vector.end(), [&](int value) { return value == minimal; });
}

bool should_run_lexmax(const Args& args) {
    return !args.skip_lexmax && args.lexmax_mode != "none";
}

bool respects_active_block(const Vec& vector, int active_start, int minimal) {
    for (int index = 0; index < active_start; ++index) {
        if (vector[index] != minimal) return false;
    }
    return true;
}

Vec leading_signature(const Matrix& block, const Vec& permutation, int leading_size) {
    Vec signature;
    signature.reserve(leading_size * (leading_size - 1) / 2);
    for (int row = 1; row < leading_size; ++row) {
        for (int column = 0; column < row; ++column) {
            signature.push_back(block[permutation[row]][permutation[column]]);
        }
    }
    return signature;
}

bool is_identity_permutation(const Vec& permutation) {
    for (int i = 0; i < static_cast<int>(permutation.size()); ++i) {
        if (permutation[i] != i) return false;
    }
    return true;
}

void sort_unique_permutations(std::vector<Vec>& permutations) {
    std::sort(permutations.begin(), permutations.end());
    permutations.erase(std::unique(permutations.begin(), permutations.end()), permutations.end());
}

Vec make_pair_permutation(int size, int first, int second) {
    Vec permutation;
    permutation.reserve(size);
    permutation.push_back(first);
    permutation.push_back(second);
    for (int item = 0; item < size; ++item) {
        if (item != first && item != second) permutation.push_back(item);
    }
    return permutation;
}

int is_lexmax_block(const Matrix& block, State& state) {
    int size = static_cast<int>(block.size());
    state.lexmax_checks += 1;
    if (size <= 1) return 1;

    std::vector<Vec> current;
    Vec best_signature;
    bool have_best = false;
    for (int first = 0; first < size; ++first) {
        for (int second = 0; second < size; ++second) {
            if (first == second) continue;
            Vec permutation = make_pair_permutation(size, first, second);
            Vec signature = leading_signature(block, permutation, 2);
            int comparison = have_best ? compare_vectors_abs(signature, best_signature) : 1;
            if (!have_best || comparison > 0) {
                current.clear();
                best_signature = signature;
                have_best = true;
            }
            if (comparison >= 0) current.push_back(std::move(permutation));
        }
    }
    sort_unique_permutations(current);
    state.lexmax_permutations_seen += static_cast<long long>(current.size());
    if (std::none_of(current.begin(), current.end(), is_identity_permutation)) return 0;

    for (int leading_size = 3; leading_size <= size; ++leading_size) {
        std::vector<Vec> next;
        have_best = false;
        best_signature.clear();
        for (const Vec& permutation : current) {
            for (int swap_position = leading_size - 1; swap_position < size; ++swap_position) {
                Vec candidate = permutation;
                std::swap(candidate[leading_size - 1], candidate[swap_position]);
                Vec signature = leading_signature(block, candidate, leading_size);
                int comparison = have_best ? compare_vectors_abs(signature, best_signature) : 1;
                if (!have_best || comparison > 0) {
                    next.clear();
                    best_signature = signature;
                    have_best = true;
                }
                if (comparison >= 0) next.push_back(std::move(candidate));
            }
        }
        sort_unique_permutations(next);
        state.lexmax_permutations_seen += static_cast<long long>(next.size());
        if (static_cast<long long>(next.size()) > state.args.lex_permutation_cap) {
            state.lexmax_inconclusive += 1;
            return 2;
        }
        if (std::none_of(next.begin(), next.end(), is_identity_permutation)) return 0;
        current = std::move(next);
    }
    return 1;
}

void append_vectors_from_prefixes(
    const std::vector<Vec>& prefixes,
    const std::vector<int>& values,
    std::vector<Vec>& out
) {
    out.clear();
    for (const Vec& prefix : prefixes) {
        for (int value : values) {
            Vec next = prefix;
            next.push_back(value);
            out.push_back(std::move(next));
        }
    }
    std::sort(out.begin(), out.end(), [](const Vec& left, const Vec& right) {
        return compare_vectors_abs(left, right) < 0;
    });
}

bool has_good_gamma(State& state, const Matrix& matrix, Int det_matrix, const std::vector<Vec>& gamma_prefixes, int emax) {
    int size = static_cast<int>(matrix.size());
    int remaining = state.args.order - size;
    if (remaining <= 0) return true;
    Int multiplier = state.pow_order_minus_one[state.args.order - size - 1];
    int n_minus_c = state.args.order - 1;
    std::vector<int> values = allowed_values(state.phi, emax);

    for (const Vec& prefix : gamma_prefixes) {
        for (int e1 : values) {
            for (int e2 : values) {
                Vec gamma = prefix;
                gamma.push_back(e1);
                gamma.push_back(e2);
                state.gamma_tests += 1;
                Matrix augmented = augment_with_gamma(matrix, gamma, 1);
                Int d = det_bareiss(augmented);
                Int positive_d = d > 0 ? d : 0;
                Int upper_bound = multiplier * (static_cast<Int>(n_minus_c) * det_matrix + static_cast<Int>(remaining) * positive_d);
                if (upper_bound >= state.threshold_det) return true;
            }
        }
    }
    return false;
}

bool has_enough_hadamard_bound(const State& state, Int det_matrix, int size) {
    int remaining = state.args.order - size;
    Int upper_bound = det_matrix;
    for (int i = 0; i < remaining; ++i) upper_bound *= state.args.order;
    return upper_bound >= state.threshold_det;
}

bool passes_bound(State& state, const Matrix& matrix, Int det_matrix, const std::vector<Vec>& gamma_prefixes, int emax) {
    if (state.args.bound_mode == "none") return true;
    if (state.args.bound_mode == "hadamard") return has_enough_hadamard_bound(state, det_matrix, static_cast<int>(matrix.size()));
    if (state.args.bound_mode == "km") return has_good_gamma(state, matrix, det_matrix, gamma_prefixes, emax);
    std::cerr << "Unknown bound mode: " << state.args.bound_mode << "\n";
    std::exit(2);
}

void write_progress(const State& state, int current_depth) {
    std::string path = state.args.output_dir + "/progress.json";
    std::ofstream out(path);
    auto elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - state.start).count();
    out << "{\n";
    out << "  \"order\": " << state.args.order << ",\n";
    out << "  \"threshold_normalized\": " << state.args.threshold_normalized << ",\n";
    out << "  \"minimal\": " << state.minimal << ",\n";
    out << "  \"phi_mode\": \"" << state.args.phi_mode << "\",\n";
    out << "  \"bound_mode\": \"" << state.args.bound_mode << "\",\n";
    out << "  \"emax_mode\": \"" << state.args.emax_mode << "\",\n";
    out << "  \"lexmax_mode\": \"" << state.args.lexmax_mode << "\",\n";
    out << "  \"skip_lexmax\": " << (state.args.skip_lexmax ? "true" : "false") << ",\n";
    out << "  \"skip_block_order\": " << (state.args.skip_block_order ? "true" : "false") << ",\n";
    out << "  \"shard_count\": " << state.args.shard_count << ",\n";
    out << "  \"shard_index\": " << state.args.shard_index << ",\n";
    out << "  \"shard_depth\": " << state.args.shard_depth << ",\n";
    out << "  \"phi\": [";
    for (size_t index = 0; index < state.phi.size(); ++index) {
        if (index) out << ", ";
        out << state.phi[index];
    }
    out << "],\n";
    out << "  \"nodes_tested\": " << state.nodes_tested << ",\n";
    out << "  \"recursion_calls\": " << state.recursion_calls << ",\n";
    out << "  \"gamma_tests\": " << state.gamma_tests << ",\n";
    out << "  \"lexmax_checks\": " << state.lexmax_checks << ",\n";
    out << "  \"lexmax_inconclusive\": " << state.lexmax_inconclusive << ",\n";
    out << "  \"lexmax_permutations_seen\": " << state.lexmax_permutations_seen << ",\n";
    out << "  \"candidates_written\": " << state.candidates_written << ",\n";
    out << "  \"shard_skipped\": " << state.shard_skipped << ",\n";
    out << "  \"current_depth\": " << current_depth << ",\n";
    out << "  \"max_depth_seen\": " << state.max_depth_seen << ",\n";
    out << "  \"stopped_by_cap\": " << (state.stopped_by_cap ? "true" : "false") << ",\n";
    out << "  \"elapsed_seconds\": " << elapsed << ",\n";
    out << "  \"levels\": [\n";
    for (size_t i = 1; i < state.levels.size(); ++i) {
        const LevelStats& level = state.levels[i];
        out << "    {\"level\": " << i
            << ", \"tested\": " << level.tested
            << ", \"accepted\": " << level.accepted
            << ", \"pruned_structure\": " << level.pruned_structure
            << ", \"pruned_row_order\": " << level.pruned_row_order
            << ", \"pruned_block_order\": " << level.pruned_block_order
            << ", \"pruned_pd\": " << level.pruned_pd
            << ", \"pruned_bound\": " << level.pruned_bound
            << ", \"pruned_lexmax\": " << level.pruned_lexmax
            << ", \"full_square_candidates\": " << level.full_square_candidates
            << ", \"full_below_threshold\": " << level.full_below_threshold
            << ", \"full_not_square\": " << level.full_not_square << "}";
        if (i + 1 < state.levels.size()) out << ",";
        out << "\n";
    }
    out << "  ]\n";
    out << "}\n";
}

void write_candidate(State& state, const Matrix& matrix, Int determinant, Int root, Int normalized) {
    state.candidate_out << "{\"normalized_determinant\": " << int_to_string(normalized)
                        << ", \"sqrt_determinant\": \"" << int_to_string(root)
                        << "\", \"gram_determinant\": \"" << int_to_string(determinant)
                        << "\", \"matrix\": [";
    for (size_t i = 0; i < matrix.size(); ++i) {
        if (i) state.candidate_out << ", ";
        state.candidate_out << "[";
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            if (j) state.candidate_out << ", ";
            state.candidate_out << matrix[i][j];
        }
        state.candidate_out << "]";
    }
    state.candidate_out << "]}\n";
    state.candidate_out.flush();
    state.candidates_written += 1;
}

int next_emax_after_accept(const Matrix& current, const Vec& vector, int current_emax, int active_start, int minimal) {
    int current_size = static_cast<int>(current.size());
    int active_size = current_size - active_start;
    if (active_size == 1 && !all_minimal(vector, minimal)) {
        return std::abs(vector.back());
    }
    return current_emax;
}

void dfs(State& state, const Matrix& matrix, const std::vector<std::vector<Vec>>& f_lists, int emax) {
    if (state.stopped_by_cap) return;
    state.recursion_calls += 1;
    int current_size = static_cast<int>(matrix.size());
    if (state.args.max_depth > 0 && current_size >= state.args.max_depth) return;
    if (current_size >= state.args.order) return;

    Blocks current_blocks = compute_blocks(matrix, state.minimal);
    int active_start = current_blocks.intervals.back().first;
    int next_size = current_size + 1;
    std::vector<int> values = allowed_values(state.phi, emax);
    std::vector<Vec> candidate_vectors;
    append_vectors_from_prefixes(f_lists[next_size - 2], values, candidate_vectors);
    std::vector<std::vector<Vec>> working_lists = f_lists;

    for (size_t vector_index = 0; vector_index < candidate_vectors.size(); ++vector_index) {
        const Vec& vector = candidate_vectors[vector_index];
        if (
            state.args.shard_count > 1
            && next_size == state.args.shard_depth
            && static_cast<int>(vector_index % state.args.shard_count) != state.args.shard_index
        ) {
            state.shard_skipped += 1;
            continue;
        }

        if (state.args.max_nodes > 0 && state.nodes_tested >= state.args.max_nodes) {
            state.stopped_by_cap = true;
            write_progress(state, current_size);
            return;
        }

        state.nodes_tested += 1;
        state.levels[next_size].tested += 1;
        state.max_depth_seen = std::max(state.max_depth_seen, next_size);
        if (state.args.progress_every > 0 && state.nodes_tested % state.args.progress_every == 0) {
            write_progress(state, next_size);
        }

        if (!respects_active_block(vector, active_start, state.minimal)) {
            state.levels[next_size].pruned_structure += 1;
            continue;
        }

        Matrix candidate = extend_matrix(matrix, vector, state.args.order);
        if (!is_row_lex_ordered(candidate)) {
            state.levels[next_size].pruned_row_order += 1;
            continue;
        }

        Blocks candidate_blocks = compute_blocks(candidate, state.minimal);
        if (!candidate_blocks.contiguous) {
            state.levels[next_size].pruned_structure += 1;
            continue;
        }
        if (!state.args.skip_block_order && !blocks_descending(candidate, candidate_blocks)) {
            state.levels[next_size].pruned_block_order += 1;
            continue;
        }

        Int determinant = det_bareiss(candidate);
        if (determinant <= 0) {
            state.levels[next_size].pruned_pd += 1;
            continue;
        }

        if (next_size == state.args.order) {
            Int root = 0;
            if (!is_square(determinant, root)) {
                state.levels[next_size].full_not_square += 1;
                continue;
            }
            Int divisor = static_cast<Int>(1) << (state.args.order - 1);
            if (root % divisor != 0) {
                state.levels[next_size].full_not_square += 1;
                continue;
            }
            Int normalized = root / divisor;
            if (normalized < state.args.threshold_normalized) {
                state.levels[next_size].full_below_threshold += 1;
                continue;
            }
            auto active_interval = candidate_blocks.intervals.back();
            Matrix active_block = submatrix_interval(candidate, active_interval.first, active_interval.second);
            int lexmax = should_run_lexmax(state.args) ? is_lexmax_block(active_block, state) : 1;
            if (lexmax == 0) {
                state.levels[next_size].pruned_lexmax += 1;
                continue;
            }
            state.levels[next_size].full_square_candidates += 1;
            state.levels[next_size].accepted += 1;
            write_candidate(state, candidate, determinant, root, normalized);
        } else {
            bool good = passes_bound(state, candidate, determinant, f_lists[next_size - 2], emax);
            if (!good) {
                state.levels[next_size].pruned_bound += 1;
                continue;
            }

            working_lists[next_size - 1].push_back(vector);

            bool starts_new_block = all_minimal(vector, state.minimal);
            bool test_partial_block = state.args.lexmax_mode == "always";
            bool test_closed_block = state.args.lexmax_mode == "closed" && starts_new_block && candidate_blocks.intervals.size() >= 2;
            if (should_run_lexmax(state.args) && (test_partial_block || test_closed_block)) {
                auto interval = candidate_blocks.intervals.back();
                if (test_closed_block) interval = candidate_blocks.intervals[candidate_blocks.intervals.size() - 2];
                Matrix block = submatrix_interval(candidate, interval.first, interval.second);
                int lexmax = is_lexmax_block(block, state);
                if (lexmax == 0) {
                    state.levels[next_size].pruned_lexmax += 1;
                    continue;
                }
            }

            state.levels[next_size].accepted += 1;
            std::vector<std::vector<Vec>> child_lists = working_lists;
            int child_emax = state.args.emax_mode == "constant"
                ? state.args.order - 2
                : next_emax_after_accept(matrix, vector, emax, active_start, state.minimal);
            dfs(state, candidate, child_lists, child_emax);
        }
    }
}

Args parse_args(int argc, char** argv) {
    Args args;
    for (int i = 1; i < argc; ++i) {
        std::string key = argv[i];
        auto require_value = [&](const std::string& name) -> std::string {
            if (i + 1 >= argc) {
                std::cerr << "Missing value for " << name << "\n";
                std::exit(2);
            }
            return argv[++i];
        };
        if (key == "--order") args.order = std::stoi(require_value(key));
        else if (key == "--threshold-normalized") args.threshold_normalized = std::stoll(require_value(key));
        else if (key == "--max-nodes") args.max_nodes = std::stoll(require_value(key));
        else if (key == "--max-depth") args.max_depth = std::stoi(require_value(key));
        else if (key == "--progress-every") args.progress_every = std::stoll(require_value(key));
        else if (key == "--lex-permutation-cap") args.lex_permutation_cap = std::stoll(require_value(key));
        else if (key == "--phi-mode") args.phi_mode = require_value(key);
        else if (key == "--bound-mode") args.bound_mode = require_value(key);
        else if (key == "--emax-mode") args.emax_mode = require_value(key);
        else if (key == "--lexmax-mode") args.lexmax_mode = require_value(key);
        else if (key == "--skip-lexmax") args.skip_lexmax = true;
        else if (key == "--skip-block-order") args.skip_block_order = true;
        else if (key == "--shard-count") args.shard_count = std::stoi(require_value(key));
        else if (key == "--shard-index") args.shard_index = std::stoi(require_value(key));
        else if (key == "--shard-depth") args.shard_depth = std::stoi(require_value(key));
        else if (key == "--output-dir") args.output_dir = require_value(key);
        else {
            std::cerr << "Unknown argument: " << key << "\n";
            std::exit(2);
        }
    }
    if (args.max_depth == 0) args.max_depth = args.order;
    if (args.shard_count < 1) {
        std::cerr << "--shard-count must be positive\n";
        std::exit(2);
    }
    if (args.shard_index < 0 || args.shard_index >= args.shard_count) {
        std::cerr << "--shard-index must be in [0, shard-count)\n";
        std::exit(2);
    }
    if (args.shard_depth == 0) args.shard_depth = std::min(args.order, 10);
    if (args.shard_depth < 2 || args.shard_depth > args.order) {
        std::cerr << "--shard-depth must be between 2 and order\n";
        std::exit(2);
    }
    return args;
}

int main(int argc, char** argv) {
    State state;
    state.args = parse_args(argc, argv);
    state.phi = make_phi(state.args.order, state.args.phi_mode);
    if (state.phi.empty()) {
        std::cerr << "Could not construct Phi for order " << state.args.order << "\n";
        return 2;
    }
    state.minimal = state.phi.front();
    state.levels.resize(state.args.order + 1);
    state.pow_order_minus_one.assign(state.args.order + 1, 1);
    for (int i = 1; i <= state.args.order; ++i) {
        state.pow_order_minus_one[i] = state.pow_order_minus_one[i - 1] * static_cast<Int>(state.args.order - 1);
    }
    Int sqrt_threshold = static_cast<Int>(state.args.threshold_normalized) * (static_cast<Int>(1) << (state.args.order - 1));
    state.threshold_det = sqrt_threshold * sqrt_threshold;
    state.start = std::chrono::steady_clock::now();

    std::error_code create_error;
    std::filesystem::create_directories(state.args.output_dir, create_error);
    if (create_error) {
        std::cerr << "Failed to create output directory: " << create_error.message() << "\n";
        return 1;
    }
    state.candidate_out.open(state.args.output_dir + "/candidates.jsonl");
    if (!state.candidate_out) {
        std::cerr << "Failed to open candidate output\n";
        return 1;
    }

    Matrix initial = {{state.args.order}};
    std::vector<std::vector<Vec>> f_lists(state.args.order + 1);
    f_lists[0].push_back(Vec{});
    int initial_emax = state.args.order - 2;

    dfs(state, initial, f_lists, initial_emax);
    write_progress(state, state.max_depth_seen);

    std::ifstream progress_in(state.args.output_dir + "/progress.json");
    std::cout << progress_in.rdbuf();
    return 0;
}
