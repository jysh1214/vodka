# Subtasks of *Add Named Pyvenv Snapshots*

## Content updates

- [x] `references/snapshot-pyvenv.md` — change labels from `[pyvenv:field]` to `[pyvenv/<name>:field]`, update collection steps to explain `<name>` (venv name or `system`), update `!file` path to `requirements-<name>.txt`
- [x] `references/snapshot.md` — update pyvenv description to mention named format `pyvenv/<name>`
- [x] `references/reproduce.md` — update pyvenv steps to iterate over each named entry under `pyvenv:`
- [x] `assets/templates/env-snapshot-example.yaml` — nest pyvenv fields under a name (e.g., `.venv`)
- [x] `references/file-reference.md` — update pyvenv example to use nested format
- [x] `README.md` — update `!file` example to use nested pyvenv format

## Verification

- [x] Grep for `[pyvenv:` (without a name segment) in active source files to confirm no stale flat-format labels remain
- [x] Run `python3 scripts/print_yaml.py` on the example template to confirm named pyvenv entries render correctly
