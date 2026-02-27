# Reproduce Dev Environment from YAML

How to reproduce a development environment from a given YAML file.

## Rules

- Skip `server` category entirely. Server-level info is not reproducible.
- If you do not know how to obtain, compile, build, or install a resource, ask the user. Do not guess.

## Priority Order

Process categories in this order:

1. `pyvenv` — Python virtual environment
2. `dep/*` or `deps/*` — Dependencies
3. All other categories (container, qemu, toolchain, exec, etc.)

Within the same category, follow the order as they appear in the YAML.

## Steps

### 1. pyvenv

1. If `module` field exists, run the `module load` command.
2. If `venv` field exists, create a virtual environment: `python3 -m venv <venv_path>` and activate it.
3. If `packages` field exists, install all packages: `pip install <package1> <package2> ...`

### 2. dep/* or deps/*

For each named dependency:

1. If `module` field exists, run the `module load` command.
2. For other fields (version, path, checksum, etc.), verify or install the dependency.
3. If you do not know how to install the dependency, ask the user for instructions.

### 3. Other categories

For each remaining category (container, qemu, toolchain, exec, etc.):

1. If `module` field exists, run the `module load` command.
2. If `startup` field exists, use it as the setup command.
3. If `build` field exists, use it as the build command.
4. If you do not know how to set up the resource, ask the user.
