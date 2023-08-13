include(CheckCXXSourceCompiles)
include(CheckCSourceCompiles)

macro(check_riscv_extensions)
  # check whether compiler supports RISC-V V extension
  check_cxx_source_compiles(
    "#include <riscv_vector.h> 
    int main() {
      return 0;
    }"
    HAVE_RVV
  )
endmacro()
