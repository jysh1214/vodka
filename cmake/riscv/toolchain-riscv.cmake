set(CMAKE_CROSSCOMPILING TRUE)
set(CMAKE_SYSTEM_NAME "Linux")
set(CMAKE_SYSTEM_PROCESSOR "riscv64")

# Avoid to use system path for cross-compile
set(CMAKE_FIND_USE_CMAKE_SYSTEM_PATH FALSE)

# Toolchain setting
set(TOOLCHAIN_PATH "" CACHE STRING "The toolchain path.")
if(NOT TOOLCHAIN_PATH)
  set(TOOLCHAIN_PATH ENV{RISCV_LINUX_TOOLCHAIN_PATH})
endif()

message(STATUS "RISC-V Linux Toolchain path: ${TOOLCHAIN_PATH}")

set(TOOLCHAIN_PREFIX "riscv64-unknown-linux-gnu" CACHE STRING "The toolchain prefix.")

# Set compiler
set(CMAKE_C_COMPILER "${TOOLCHAIN_PATH}/bin/${TOOLCHAIN_PREFIX}-clang")
set(CMAKE_CXX_COMPILER "${TOOLCHAIN_PATH}/bin/${TOOLCHAIN_PREFIX}-clang++")

# Disable auto-vectorize
add_compile_options(-fno-vectorize -fno-slp-vectorize)
