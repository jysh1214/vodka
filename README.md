# VODKA 🍾 #

Rewrite algorithms using modern C++.

## Prerequisites ##

- cmake
- clang-format  (formatting tool)
- ninja         (for linux)
- Visual Studio (for windows)

## Building ##

  ### Linux ###

  ```bash
  # config
  cmake -G Ninja -B build .

  # build
  cmake --build build
  ```

  ### Windows ###

  ```bash
  cmake -G "Visual Studio 17 2022" `
    -B build `
    -A x64 `
    .
  ```

  Open the `.sln` file, and use `Visual Studio` to development.

  ### (Optional) Speedup Building ###

  **Enable CCACHE**
  The CCACHE could speed up recompilation by caching previous compilations and detecting when the same compilation is being done again. Setup the `CMAKE_CXX_COMPILER_LAUNCHER` with `ccache` tool in cmake command.
  ```bash
  -D CMAKE_CXX_COMPILER_LAUNCHER=ccache
  ```

  **Set the Process Number**
  We could set the `CMAKE_BUILD_PARALLEL_LEVEL` environment variable to use more process number to speed up building process.
  ```bash
  export CMAKE_BUILD_PARALLEL_LEVEL=16
  ```

## CMake Options ##

- `BUILD_SHARED_LIBS`: Build & link with dynamic library. (Default OFF)
- `BUILD_TESTS`: Build unit tests. (Default ON)
- `BUILD_BENCHMARK`: Build benchmarking. (Default ON)
- `NO_EXCEPTION`: Disable throw exceptions. (Default OFF)
- `WARNING_AS_ERROR`: Warning as error. (Default ON)

## Overview of The Repo ##

- `arch`
- `benchamrk`
- `cmake`
- `doc`
- `library`
- `script`
- `test`

## Formatting ##

We use `clang-format` to help us keep the codes clean.

Usage:
```bash
# in the vodka root
./script/git/reformat.sh
```

The header files include order is same as lexicographical order.

## Naming Conventions ##

All functions and arguments use `snake_case`. (e.g., `my_var`)

All class and struct use `CamelCase`. (e.g., `MyClass`)
