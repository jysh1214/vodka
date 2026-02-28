---
name: vodka
description: Capture and organize a complete snapshot of the user's development environment into a structured YAML format. Use when the user wants to snapshot their dev environment.
allowed-tools: Bash, Read, Write, Edit, Glob
---

# vodka - Dev Environment Snapshot

Read these references first:

- [references/snapshot.md](references/snapshot.md) — categories and fields overview
- [references/snapshot-server.md](references/snapshot-server.md) — server auto-collect steps
- [references/snapshot-pyvenv.md](references/snapshot-pyvenv.md) — Python virtual environment fields
- [references/snapshot-container-template.md](references/snapshot-container-template.md) — Container template
- [references/snapshot-qemu-template.md](references/snapshot-qemu-template.md) — QEMU template
- [references/snapshot-toolchain-template.md](references/snapshot-toolchain-template.md) — Toolchain template
- [references/snapshot-exec-template.md](references/snapshot-exec-template.md) — Executable Binaries template
- [references/snapshot-dep-template.md](references/snapshot-dep-template.md) — Dependencies template
- [references/reproduce.md](references/reproduce.md) — reproduce dev environment from YAML
- [references/file-reference.md](references/file-reference.md) — `!file` tag for external file references

## Workflow

1. When the skill is triggered, immediately auto-collect server info and create `.vodka/env-snapshot-{YYYY-MM-DD-HH-MM-SS}.yaml`, follow [references/snapshot-server.md](references/snapshot-server.md).
2. If users want to snapshot pyvenv, follow [references/snapshot-pyvenv.md](references/snapshot-pyvenv.md).
3. Users can add snapshots at any time. Each snapshot creates a new timestamped file. Multiple entries at once is fine.
4. If users want to show the snapshot, run `python3 scripts/print_yaml.py` to display it as a table.
5. If users want to extract large values to files, read the latest `.vodka/env-snapshot-*.yaml`, save large values to separate files under `.vodka/`, and replace them with `!file` references. See [references/file-reference.md](references/file-reference.md).
6. If users want to reproduce the dev environment from a YAML file, follow [references/reproduce.md](references/reproduce.md).

## Rules

- Always auto-collect server info first before asking for manual input.
- Accept labeled input in any order. Merge and deduplicate.
- If the user pastes raw commands without labels, ask them to clarify which category and field the command belongs to.
- For template categories, group all fields under the same `category/name` together.
- Save the output as a file (`.vodka/env-snapshot-{YYYY-MM-DD-HH-MM-SS}.yaml`). Follow the format in [assets/templates/env-snapshot-example.yaml](assets/templates/env-snapshot-example.yaml).
- For large field values, use `!file` to store content in a separate file under `.vodka/`. See [references/file-reference.md](references/file-reference.md).
