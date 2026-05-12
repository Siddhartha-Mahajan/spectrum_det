CXX ?= clang++
CXXFLAGS ?= -O3 -std=c++17 -Wall -Wextra -pedantic

all: paper_reproduction_generator

paper_reproduction_generator: paper_reproduction_generator.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm -f paper_reproduction_generator
