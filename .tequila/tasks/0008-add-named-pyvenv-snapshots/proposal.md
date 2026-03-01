# Proposal of *Add Named Pyvenv Snapshots*

## Motivation

A project may use multiple Python virtual environments. The current flat `pyvenv:field` format only supports a single environment. Switching to `pyvenv/<name>:field` allows capturing multiple named environments in the same snapshot, consistent with how template categories (dep, container, etc.) already work. The name is the venv name from `python -m venv <name>`, or `system` for system-wide Python.

## Summary

- **BREAKING** — Change pyvenv label format from `[pyvenv:field]` to `[pyvenv/<name>:field]`
- **BREAKING** — Change YAML structure from flat `pyvenv:` to nested `pyvenv: <name>: field:`
- Update `references/snapshot-pyvenv.md` — labels, collection steps, examples
- Update `references/snapshot.md` — pyvenv description to reflect named format
- Update `references/reproduce.md` — pyvenv reproduction steps to iterate over named entries
- Update `assets/templates/env-snapshot-example.yaml` — use nested pyvenv structure
- Update `SKILL.md` if needed
- Update `references/file-reference.md` example if needed

## Impact

- Affected code: `references/snapshot-pyvenv.md`, `references/snapshot.md`, `references/reproduce.md`, `assets/templates/env-snapshot-example.yaml`, `references/file-reference.md`, possibly `SKILL.md`, `scripts/print_yaml.py`
