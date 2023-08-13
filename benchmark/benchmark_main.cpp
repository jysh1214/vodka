/**
 * @file benchmark_main.cpp
 * @author Alex Chiang
 * @brief Main entry point for benchmark framework.
 */
#include <benchmark/benchmark.h>

int main(int argc, char **argv) {
  ::benchmark::Initialize(&argc, argv);
  ::benchmark::RunSpecifiedBenchmarks();

  return EXIT_SUCCESS;
}
