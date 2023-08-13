set(ARCH ${CMAKE_SYSTEM_PROCESSOR})

if("${ARCH}" MATCHES "(x86_64|AMD64|i[3-6]86)")
  set(AMD64 TRUE)
elseif("${ARCH}" MATCHES "(riscv(32|64)|riscv)")
  set(RISCV TRUE)
else()
  message(FATAL_ERROR "No support ${ARCH}.")
endif()
