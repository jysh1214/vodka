# Proposal of *Add Reproduce Target Directory*

## Motivation

The reproduce workflow (`references/reproduce.md`) currently has no concept of a target directory. Commands run in whatever directory the user happens to be in, and `pyvenv` entries without a `venv` field install packages directly into the system Python. This is risky and unpredictable — users need a way to specify where the reproduced environment should land.

## Summary

- Add a target directory parameter to the reproduce workflow in `references/reproduce.md`
- When a target directory is provided, create `pyvenv` virtual environments under `<target>/<name>` (via `python3 -m venv <name>` run inside `<target>`, using the Python resolved after any `module load` step) instead of relying on the `venv` field or falling back to the system Python
- Other categories (dep, container, toolchain, exec, etc.) should run within the target directory context where applicable

## Impact

- Affected code: `references/reproduce.md`
