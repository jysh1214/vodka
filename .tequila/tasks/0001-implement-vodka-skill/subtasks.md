# Subtasks of *Implement Vodka Skill*

## Skill Structure

- [x] Create `README.md` with usage instructions and labeled input examples
- [x] Create `SKILL.md` with skill overview, workflow, and rules
- [x] Create `references/DEV_ENV_SNAPSHOT_CATEGORIES_FIELDS.md` with all category/field definitions

## Validation

- [x] Run the skill end-to-end: trigger a full snapshot and verify `.vodka/env-snapshot.yaml` is produced with auto-collected server and Python fields
- [x] Test incremental snapshot: add a manual `[toolchain:name]` entry and verify it merges into the existing file
