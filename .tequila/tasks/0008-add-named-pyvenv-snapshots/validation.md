# Validation of *Add Named Pyvenv Snapshots*

## Validation Method

Manual review of all changed files to confirm pyvenv uses the named `pyvenv/<name>` format consistently, plus automated grep and script checks.

## Steps

1. Review `references/snapshot-pyvenv.md` — labels are `[pyvenv/<name>:field]`, `<name>` explanation present, `!file` path uses `requirements-<name>.txt`
2. Review `references/snapshot.md` — heading says `pyvenv/<name>`, description mentions venv name or `system`
3. Review `references/reproduce.md` — priority order says `pyvenv/*`, steps iterate over each named entry
4. Review `assets/templates/env-snapshot-example.yaml` — pyvenv fields are nested under `.venv:`
5. Review `references/file-reference.md` — pyvenv example uses nested format with `requirements-.venv.txt`
6. Review `README.md` — `!file` example uses nested pyvenv format
7. Grep for stale flat-format `[pyvenv:field]` labels in active source files (excluding `.tequila/`) — no hits
8. Run `python3 scripts/print_yaml.py assets/templates/env-snapshot-example.yaml` — pyvenv rows show `.venv` in Name column

## Expected Outcome

All files use the named `pyvenv/<name>` format. No stale flat-format labels remain in active source files. The print script renders pyvenv entries with a name.

## Result

- Status: PASS
- User confirmed all changes are correct. Generated a new snapshot with pyvenv/system to verify the named format end-to-end.
