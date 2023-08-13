set(ARCH_HEADERS)
set(ARCH_SOURCES)

set(FIND_OPTIMIZATION FALSE)

if(AMD64)

elseif(RISCV)
  include(riscv/check-riscv-extension)
  check_riscv_extensions()
  if(HAVE_RVV)
    list(APPEND ARCH_HEADERS ${ARCH_DIR}/histogram_rvv.h)
    list(APPEND ARCH_SOURCES ${ARCH_DIR}/histogram_rvv.cpp)
    set(ARCH_DIR ${ARCH_DIR}/riscv)
    set(FIND_OPTIMIZATION TRUE)
  endif()
endif()

if(NOT FIND_OPTIMIZATION)
  message(STATUS "Cannot find any optimizatation for ${ARCH}.")
  set(ARCH_DIR ${ARCH_DIR}/generic)
  list(APPEND ARCH_HEADERS ${ARCH_DIR}/generic.h)
  list(APPEND ARCH_SOURCES ${ARCH_DIR}/generic.cpp)
endif()

add_library(ArchKernel STATIC ${ARCH_HEADERS} ${ARCH_SOURCES})
add_library(Vodka::ArchKernel ALIAS ArchKernel)
