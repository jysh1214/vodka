# Dev Environment Snapshot

## Auto-Collect

### System (`system`)

See [snapshot-system.md](snapshot-system.md) for detailed collection steps.

## Manual Input

### Python Virtual Environment (`pyvenv/<name>`)

See [snapshot-pyvenv.md](snapshot-pyvenv.md) for detailed collection steps. `<name>` is the venv name or `system` for system-wide Python.

### Templates

The following categories are templates. Users can flexibly add any snapshot fields under `[category/name:field]`.

- [snapshot-dep-template.md](snapshot-dep-template.md) — Dependencies
- [snapshot-container-template.md](snapshot-container-template.md) — Container
- [snapshot-qemu-template.md](snapshot-qemu-template.md) — QEMU
- [snapshot-toolchain-template.md](snapshot-toolchain-template.md) — Toolchain
- [snapshot-exec-template.md](snapshot-exec-template.md) — Executable Binaries

Users can create any `category/name` and add arbitrary fields.
