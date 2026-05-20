CXX ?= clang++
CXXFLAGS ?= -O3 -std=c++17 -Wall -Wextra -pedantic
NATIVE_CXXFLAGS ?= $(CXXFLAGS) -march=native -flto

all: optimized_reproduction_generator

optimized_reproduction_generator: optimized_reproduction_generator.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

optimized_reproduction_generator_native: optimized_reproduction_generator.cpp
	$(CXX) $(NATIVE_CXXFLAGS) $< -o $@

clean:
	rm -f optimized_reproduction_generator optimized_reproduction_generator_native
