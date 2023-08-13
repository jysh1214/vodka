cmake_minimum_required(VERSION ${CMAKE_MIN_VERSION})

include(FetchContent)

find_package(benchmark QUIET)
# Fetch google benchmark source code from official repository
if(NOT benchmark_FOUND)
  set(GBENCHMARK_REPOSITORY https://github.com/google/benchmark.git)
  set(GBENCHMARK_TAG "v1.7.1")

  FetchContent_Declare(benchmark
    GIT_REPOSITORY ${GBENCHMARK_REPOSITORY}
    GIT_TAG ${GBENCHMARK_TAG}
  )

  FetchContent_GetProperties(benchmark)
  if(NOT benchmark_POPULATED)
    FetchContent_Populate(benchmark)
    add_subdirectory(${benchmark_SOURCE_DIR} ${benchmark_BINARY_DIR} EXCLUDE_FROM_ALL)
  endif()
endif()

add_executable(vodka_benchmark
  benchmark_main.cpp
)

target_compile_definitions(vodka_benchmark PRIVATE -DBENCHMARK_STATIC_DEFINE)
target_include_directories(vodka_benchmark PRIVATE
  ${PROJECT_SOURCE_DIR}
  ${PROJECT_BINARY_DIR}
  ${ARCH_DIR}
  ${LIBRARY_DIR}
  ${benchmark_SOURCE_DIR}/benchmark/include
)

target_link_libraries(vodka_benchmark PRIVATE Vodka::Library Vodka::ArchKernel benchmark::benchmark)
