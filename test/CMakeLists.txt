cmake_minimum_required(VERSION ${CMAKE_MIN_VERSION})

include(FetchContent)

find_package(Gtest QUIET)
# Fetch google test source code from official repository
if(NOT Gtest_FOUND)
  set(GTEST_REPOSITORY https://github.com/google/googletest.git)
  set(GTEST_TAG "release-1.10.0")

  FetchContent_Declare(googletest
    GIT_REPOSITORY ${GTEST_REPOSITORY}
    GIT_TAG ${GTEST_TAG}
  )

  FetchContent_GetProperties(googletest)
  if(NOT googletest_POPULATED)
    FetchContent_Populate(googletest)
    add_subdirectory(${googletest_SOURCE_DIR} ${googletest_BINARY_DIR} EXCLUDE_FROM_ALL)
  endif()
endif()

add_executable(vodka_test
  test_load_buffer.cpp
  test_main.cpp
)

target_include_directories(vodka_test PRIVATE
  ${PROJECT_SOURCE_DIR}
  ${PROJECT_BINARY_DIR}
  ${ARCH_DIR}
  ${LIBRARY_DIR}
)

target_link_libraries(vodka_test PRIVATE Vodka::Library Vodka::ArchKernel gtest)
