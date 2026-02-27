# Subtasks of *Add File Reference in YAML*

## Implementation

- [x] Create `references/file-reference.md` documenting the `!file` tag syntax and usage rules
- [x] Update `SKILL.md` to reference `file-reference.md` and add a rule for when to use `!file`
- [x] Update `README.md` to mention `!file` support
- [x] Update `assets/templates/env-snapshot-example.yaml` to show `!file` usage
- [x] Update `scripts/print_yaml.py` to resolve `!file` references when displaying
- [x] Update `references/reproduce.md` to handle `!file` references when reproducing

## Validation

- [x] Run `print_yaml.py` against the updated example YAML and verify `!file` references resolve correctly
