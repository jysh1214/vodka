# File Reference (`!file` Tag)

Support for storing large snapshot values in separate files using the `!file` YAML tag.

## Syntax

```yaml
field: !file path/to/file
```

The path is relative to the snapshot subfolder (e.g., `.vodka/{snapshot-id}-{timestamp}/`).

## When to Use

- Use `!file` when a field value is large (e.g., `pip freeze` output, long package lists).
- Store referenced files in the snapshot subfolder alongside `env-snapshot.yaml`.
- Inline values are still fully supported — `!file` is optional.

## Examples

```yaml
pyvenv:
  .venv:
    packages: !file requirements-.venv.txt

toolchain:
  arm-gcc:
    checksum: !file arm-gcc.md5
```

## Rules

- Referenced files must exist at the specified path.
- Paths are relative to the snapshot subfolder.
- No nested references — a `!file` target cannot itself contain `!file` tags.
- When reading a `!file` reference, load the entire file content as the field value.
