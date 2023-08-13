/**
 * @file test_main.cpp
 * @author Alex Chiang
 * @brief Main entry point for test framework.
 */
#include <gtest/gtest.h>

GTEST_API_ int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
