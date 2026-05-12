CXX ?= clang++
CXXFLAGS ?= -O3 -std=c++17 -Wall -Wextra -pedantic

all: native_gram_generator

native_gram_generator: native_gram_generator.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm -f native_gram_generator
