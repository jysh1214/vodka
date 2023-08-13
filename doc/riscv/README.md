# Build VODKA 🍾 with Upstream RISC-V Toolchain #

## Enviroment ##

- Linux

## Build GNU RISC-V Toolchain ##

Please refer the [riscv-gnu-toolchain](https://github.com/riscv-collab/riscv-gnu-toolchain#llvm--clang) to build linux toolchain with LLVM.
`RISCV_LINUX_TOOLCHAIN_PATH` would be the install path.

## Build ##

Build:
```bash
cmake -G Ninja -B build-riscv \
  -D CMAKE_TOOLCHAIN_FILE=cmake/riscv/toolchain-riscv.cmake \
  -D TOOLCHAIN_PATH="$RISCV_LINUX_TOOLCHAIN_PATH" \
  .

cmake --build ./build-riscv
```

Use `vodka` in user mode `QEMU`:
```bash
export QEMU_CPU_OPTION="rv64,zba=true,zbb=true,zbc=true,zbs=true,v=true,vlen=512,elen=64,vext_spec=v1.0"
$RISCV_LINUX_TOOLCHAIN_PATH/bin/qemu-riscv64 \
  -cpu ${QEMU_CPU_OPTION} \
  -L $RISCV_LINUX_TOOLCHAIN_PATH/sysroot \
  build-riscv/benchmark/benchmark_vodka
```

```bash
export QEMU_CPU_OPTION="rv64,zba=true,zbb=true,zbc=true,zbs=true,v=true,vlen=512,elen=64,vext_spec=v1.0"
$RISCV_LINUX_TOOLCHAIN_PATH/bin/qemu-riscv64 \
  -cpu ${QEMU_CPU_OPTION} \
  -L $RISCV_LINUX_TOOLCHAIN_PATH/sysroot \
  build-riscv/test/test_vodka
```
