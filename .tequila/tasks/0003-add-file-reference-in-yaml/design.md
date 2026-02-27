# Design of *Add File Reference in YAML*

## Context

Some snapshot fields contain large values (e.g., `pip freeze` lists, checksums). Inlining everything in `.vodka/env-snapshot.yaml` makes it bloated. The `!file` YAML tag allows values to be stored in separate files and referenced from the snapshot.

## Goals / Non-Goals

- Goals:
  - Define the `!file` tag syntax and document it in a new reference doc
  - Update `SKILL.md` rules to instruct the AI when to use `!file`
  - Update `scripts/print_yaml.py` to resolve `!file` references
  - Update `assets/templates/env-snapshot-example.yaml` to show `!file` usage
  - Update `references/reproduce.md` to handle `!file` references
- Non-goals:
  - Forcing `!file` for all values — inline values remain fully supported
  - Nested file references (a `!file` target cannot itself contain `!file` tags)

## Decisions

- Decision: Use `!file` YAML custom tag syntax
  - Rationale: YAML custom tags are the standard mechanism for type extensions. `!file .vodka/requirements.txt` is clean and unambiguous.
- Decision: Store referenced files under `.vodka/` alongside the snapshot
  - Rationale: Keeps all snapshot data co-located and portable.
- Decision: The AI decides when to use `!file` based on value size, but the user can also explicitly request it
  - Rationale: Flexible — auto for convenience, manual for control.

## Risks / Trade-Offs

- `yaml.safe_load` does not handle custom tags by default. `print_yaml.py` needs a custom loader to resolve `!file` references.
- Referenced files must exist at the expected path when the snapshot is read. Missing files should produce a clear error.
