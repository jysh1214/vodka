# Proposal of *Align YAML Order with Reproduce Priority*

## Motivation

The reproduction priority in `references/reproduce.md` is: `pyvenv` → `dep/*` → all others. However, the example YAML template (`assets/templates/env-snapshot-example.yaml`) places `dep` last, after container, qemu, toolchain, and exec. When reading a snapshot, the field order should match the reproduction order so that the file reads top-to-bottom in the same sequence it would be reproduced.

## Summary

- Reorder `assets/templates/env-snapshot-example.yaml` to: `server`, `pyvenv`, `dep`, then remaining categories (container, qemu, toolchain, exec)
- Update `references/snapshot.md` to list categories in the same priority order
- Reorder the existing `.vodka/env-snapshot-*.yaml` file if it contains categories that are out of order

## Impact

- Affected code: `assets/templates/env-snapshot-example.yaml`, `references/snapshot.md`, existing snapshot files
