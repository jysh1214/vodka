# Subtasks of *Add Snapshot Naming and Update Structure*

## Documentation updates

- [x] `SKILL.md` — update workflow to describe new folder structure and snapshot naming convention; update rules for file paths; update usage prompt to "snapshot the development environment for {description}"; describe merge behavior: adding entries creates a new folder with same snapshot-id but fresh timestamp
- [x] `README.md` — update usage examples with new folder structure, snapshot naming, and optional Jira ticket ID
- [x] `references/snapshot-system.md` — update step 4 path from `.vodka/env-snapshot-{YYYY-MM-DD-HH-MM-SS}.yaml` to `.vodka/{snapshot-id}/env-snapshot.yaml`
- [x] `references/snapshot-pyvenv.md` — update steps 2–3 paths; `!file` references are now relative to the snapshot subfolder
- [x] `references/file-reference.md` — change `!file` path base from `.vodka/` to the snapshot subfolder
- [x] `references/reproduce.md` — update `!file` rule to note paths are relative to the snapshot subfolder

## Script updates

- [x] `scripts/print_yaml.py` — update `find_latest_snapshot()` to search `.vodka/*/env-snapshot.yaml` sorted by timestamp suffix; update `resolve_value()` base_dir to use the snapshot's subfolder

## Migration

- [x] Migrate existing `.vodka/` contents into a new subfolder (e.g., `.vodka/snapshot-dev-environment-2026-03-01-07-09-11/`)

## Verification

- [x] Run `python3 scripts/print_yaml.py` to confirm the script finds and renders the migrated snapshot correctly
- [x] Review all updated docs for consistent path references
