# __     _____  ____  _  __    _
# \ \   / / _ \|  _ \| |/ /   / \
#  \ \ / / | | | | | | ' /   / _ \
#   \ V /| |_| | |_| | . \  / ___ \
#    \_/  \___/|____/|_|\_\/_/   \_\
#
# VODKA Project.
#
# Author: Alex Chiang
#
set(CMAKE_MIN_VERSION 3.21)
cmake_minimum_required(VERSION ${CMAKE_MIN_VERSION})
message(STATUS "Using CMake version ${CMAKE_VERSION}")

project(vodka C CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(DEFAULT_CMAKE_BUILD_TYPE Release)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 23)

set(ARCH_DIR ${PROJECT_SOURCE_DIR}/arch)
set(LIBRARY_DIR ${PROJECT_SOURCE_DIR}/library)

# Options
option(BUILD_SHARED_LIBS "Build & link with dynamic library." OFF)
option(BUILD_TEST "" ON)
option(BUILD_BENCHMARK "" ON)
option(NO_EXCEPTION "" OFF)
option(WARNING_AS_ERROR "" ON)

if(CMAKE_TOOLCHAIN_FILE)
  message(STATUS "Using CMake toolchain: ${CMAKE_TOOLCHAIN_FILE}")
endif()

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR}/cmake)

# Detect architectures
include(detect-arch)
# Add optimized kernels for the specific architecture
include(add-arch-kernel)
# Set compiler flags
include(set-compiler-flags)

add_subdirectory(library)

# Test
if(BUILD_TEST)
  add_subdirectory(test)
endif()

# Benchmark
if(BUILD_BENCHMARK)
  add_subdirectory(benchmark)
endif()



