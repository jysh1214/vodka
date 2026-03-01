# Subtasks of *Add Run Expect List Support*

## Script

- [x] Update `scripts/extract_steps.py`: handle `run` as string or list, collect `expect` field (string or list), attach checks to the last run step in each entry

## Documentation

- [x] Update `references/snapshot-exec-template.md`: add `expect` field to the fields table and example
- [x] Update `assets/templates/env-snapshot-example.yaml`: change `exec/firmware` to use list `run` and add `expect`
