# Proposal of *Add File Reference in YAML*

## Motivation

Some snapshot values can be very large (e.g., `pip freeze` output with dozens of packages, or binary checksums). Embedding all of this inline in `.vodka/env-snapshot.yaml` makes the file bloated and hard to read. By supporting file references via the `!file` YAML tag, large values can be stored in separate files and referenced from the snapshot.

## Summary

- Support `!file path` syntax in `.vodka/env-snapshot.yaml` to reference external files
- Example: `packages: !file .vodka/requirements.txt` instead of inlining all packages
- When snapshotting, the AI saves large values to separate files under `.vodka/` and writes a `!file` reference in the YAML
- When reproducing, the AI reads the referenced file to get the actual value
- When showing (print_yaml.py), resolve `!file` references to display the content
- Update `SKILL.md`, `README.md`, reference docs, example YAML, and `scripts/print_yaml.py`

## Impact

- Affected code: `SKILL.md`, `README.md`, `references/`, `assets/templates/env-snapshot-example.yaml`, `scripts/print_yaml.py`
- New files under `.vodka/` for referenced content (e.g., `.vodka/requirements.txt`)
- No breaking changes — inline values still work as before
