#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
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
    std::string output_dir = "outputs/smoke";
};

struct LevelStats {
    long long tested = 0;
    long long accepted = 0;
    long long pruned_pd = 0;
    long long pruned_bound = 0;
    long long full_square_candidates = 0;
    long long full_below_threshold = 0;
    long long full_not_square = 0;
};

struct State {
    Args args;
    std::vector<int> phi;
    Int threshold_det = 0;
    std::vector<Int> pow_order_minus_one;
    std::vector<LevelStats> levels;
    long long nodes_tested = 0;
    long long recursion_calls = 0;
    long long candidates_written = 0;
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

Int abs_int(Int value) {
    return value < 0 ? -value : value;
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

Matrix extend_matrix(const Matrix& matrix, const Vec& vector, int order) {
    int r = static_cast<int>(matrix.size());
    Matrix candidate(r + 1, std::vector<int>(r + 1, order));
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < r; ++j) candidate[i][j] = matrix[i][j];
    }
    for (int i = 0; i < r; ++i) {
        candidate[i][r] = vector[i];
        candidate[r][i] = vector[i];
    }
    return candidate;
}

Matrix augment_with_gamma(const Matrix& matrix, const Vec& gamma, int c) {
    int r = static_cast<int>(matrix.size());
    Matrix augmented(r + 1, std::vector<int>(r + 1, c));
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < r; ++j) augmented[i][j] = matrix[i][j];
    }
    for (int i = 0; i < r; ++i) {
        augmented[i][r] = gamma[i];
        augmented[r][i] = gamma[i];
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

std::vector<int> odd_order_phi(int order) {
    std::vector<int> phi;
    if (order % 4 == 1) {
        for (int value = 2 - order; value <= 1; value += 4) phi.push_back(value);
    } else if (order % 4 == 3) {
        for (int value = 2 - order; value <= 3; value += 4) phi.push_back(value);
    } else {
        for (int value = -order; value <= order; value += 2) {
            if ((value - order) % 4 == 0) phi.push_back(value);
        }
    }
    return phi;
}

void append_vectors_from_prefixes(
    const std::vector<Vec>& prefixes,
    const std::vector<int>& phi,
    int max_abs,
    std::vector<Vec>& out
) {
    out.clear();
    for (const Vec& prefix : prefixes) {
        for (int value : phi) {
            if (std::abs(value) <= max_abs) {
                Vec next = prefix;
                next.push_back(value);
                out.push_back(std::move(next));
            }
        }
    }
}

bool has_good_gamma(const State& state, const Matrix& matrix, Int det_matrix, const std::vector<Vec>& gamma_prefixes) {
    int size = static_cast<int>(matrix.size());
    int remaining = state.args.order - size;
    if (remaining <= 0) return true;
    Int multiplier = state.pow_order_minus_one[state.args.order - size - 1];
    int n_minus_c = state.args.order - 1;

    for (const Vec& prefix : gamma_prefixes) {
        for (int e1 : state.phi) {
            for (int e2 : state.phi) {
                Vec gamma = prefix;
                gamma.push_back(e1);
                gamma.push_back(e2);
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

void write_progress(const State& state, int current_depth) {
    std::string path = state.args.output_dir + "/progress.json";
    std::ofstream out(path);
    auto elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - state.start).count();
    out << "{\n";
    out << "  \"order\": " << state.args.order << ",\n";
    out << "  \"threshold_normalized\": " << state.args.threshold_normalized << ",\n";
    out << "  \"nodes_tested\": " << state.nodes_tested << ",\n";
    out << "  \"recursion_calls\": " << state.recursion_calls << ",\n";
    out << "  \"candidates_written\": " << state.candidates_written << ",\n";
    out << "  \"current_depth\": " << current_depth << ",\n";
    out << "  \"max_depth_seen\": " << state.max_depth_seen << ",\n";
    out << "  \"stopped_by_cap\": " << (state.stopped_by_cap ? "true" : "false") << ",\n";
    out << "  \"elapsed_seconds\": " << elapsed << ",\n";
    out << "  \"levels\": [\n";
    for (size_t i = 1; i < state.levels.size(); ++i) {
        const LevelStats& level = state.levels[i];
        out << "    {\"level\": " << i << ", \"tested\": " << level.tested
            << ", \"accepted\": " << level.accepted
            << ", \"pruned_pd\": " << level.pruned_pd
            << ", \"pruned_bound\": " << level.pruned_bound
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

void dfs(State& state, const Matrix& matrix, const std::vector<std::vector<Vec>>& f_lists, int max_abs) {
    if (state.stopped_by_cap) return;
    state.recursion_calls += 1;
    int current_size = static_cast<int>(matrix.size());
    if (state.args.max_depth > 0 && current_size >= state.args.max_depth) return;
    if (current_size >= state.args.order) return;

    int next_size = current_size + 1;
    std::vector<Vec> candidate_vectors;
    append_vectors_from_prefixes(f_lists[next_size - 2], state.phi, max_abs, candidate_vectors);
    std::vector<std::vector<Vec>> working_lists = f_lists;

    for (const Vec& vector : candidate_vectors) {
        if (state.nodes_tested >= state.args.max_nodes) {
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
        Matrix candidate = extend_matrix(matrix, vector, state.args.order);
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
            state.levels[next_size].full_square_candidates += 1;
            state.levels[next_size].accepted += 1;
            write_candidate(state, candidate, determinant, root, normalized);
        } else {
            bool good = has_good_gamma(state, candidate, determinant, f_lists[next_size - 2]);
            if (!good) {
                state.levels[next_size].pruned_bound += 1;
                continue;
            }
            state.levels[next_size].accepted += 1;
            working_lists[next_size - 1].push_back(vector);
            std::vector<std::vector<Vec>> child_lists = working_lists;
            dfs(state, candidate, child_lists, max_abs);
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
        else if (key == "--output-dir") args.output_dir = require_value(key);
        else {
            std::cerr << "Unknown argument: " << key << "\n";
            std::exit(2);
        }
    }
    if (args.max_depth == 0) args.max_depth = args.order;
    return args;
}

int main(int argc, char** argv) {
    State state;
    state.args = parse_args(argc, argv);
    state.phi = odd_order_phi(state.args.order);
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
        std::cerr << "Failed to create output directory\n";
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
    int max_abs = state.args.order - 2;

    dfs(state, initial, f_lists, max_abs);
    write_progress(state, state.max_depth_seen);

    std::ifstream progress_in(state.args.output_dir + "/progress.json");
    std::cout << progress_in.rdbuf();
    return 0;
}
