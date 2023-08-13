#include "load_buffer.h"

LoadBuffer::LoadBuffer(std::string_view filename, const std::size_t buffer_size,
                       std::ios::openmode mode)
    : file(filename.data(), mode), buffer_size(buffer_size) {
  if (!file) {
    std::string err_msg{"ERROR: Open the file failed."};
    VODKA_DISPLAY << err_msg << "\n";
    VODKA_THROW(std::runtime_error(err_msg));
  }

  /* Calculate the file size */
  file.seekg(0, std::ifstream::end);
  left_size = file.tellg();
  /* Seek the file from the beginning */
  file.seekg(0, std::ifstream::beg);
}

const std::size_t LoadBuffer::load_next() {
  std::size_t load_size = std::min(left_size, buffer_size);
  file.read(buffer.data(), load_size);

  std::size_t read_size = file.gcount();
  left_size -= read_size;
  assert(left_size >= 0);

  return read_size;
}

const std::size_t LoadBuffer::get_left_size() { return left_size; }
