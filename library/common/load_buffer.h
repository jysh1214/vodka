/**
 * @file load_buffer.h
 * @author Alex Chiang
 * @brief Load buffer header file.
 */
#ifndef LOAD_BUFFER_H
#define LOAD_BUFFER_H

#include "../vodka.h"

#include <cassert>
#include <fstream>
#include <string_view>
#include <vector>

#include "../vodka.h"

struct LoadBuffer {

public:
  explicit LoadBuffer(std::string_view filename, const std::size_t buffer_size,
                      std::ios::openmode mode = std::ios::in |
                                                std::ios::binary);

  const std::size_t load_next();
  const std::size_t get_left_size();

private:
  std::ifstream file;
  std::size_t left_size;
  std::vector<char> buffer;
  std::size_t buffer_size;
};

#endif // LOAD_BUFFER_H
