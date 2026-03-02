# Subtasks of *Refactor Reproduce to Generate Scripts*

## Update SKILL.md

- [x] Rewrite workflow step 6 to remove `{target}` and describe new usage: `Follow vodka skill, reproduce dev environment from {snapshot-id}`
- [x] Remove step 7 (extract experiment steps) — experiment steps extraction is now part of the reproduce flow

## Rewrite references/reproduce.md

- [x] Remove the "Target Directory" section entirely
- [x] Rewrite the document as a script-generation guide with three output sections: `reproduce.sh`, `experiment-steps.sh`, `run_qemu.py`
- [x] Document `reproduce.sh` generation: covers `pyvenv`, `dep`/`deps`, and all other categories except `exec` and `system`, following the existing priority order
- [x] Document `experiment-steps.sh` generation: covers `exec` section only, translating `run`, `expect`, `cd`, `startup`, and `build` fields into shell commands
- [x] Document `run_qemu.py` generation: produced only when `exec` entries involve QEMU commands; uses `pexpect` to spawn and interact with QEMU; called from `experiment-steps.sh`
- [x] Document the notification step: inform user that scripts are generated in `.vodka/{snapshot-id}-{timestamp}/` and ready to use

## Notes

- `system` category remains skipped (not reproducible)
- Scripts are generated into `.vodka/{snapshot-id}-{timestamp}/` alongside `env-snapshot.yaml`
- `!file` references must be resolved when generating script content
- QEMU detection: check if exec entry commands contain `qemu` (case-insensitive) or if the entry references a `qemu/*` category
