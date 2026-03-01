# Validation of *Rename Server to System*

## Validation Method

Manual review of all changed files to confirm every `server` → `system` rename is correct, plus automated grep and script checks.

## Steps

1. Review `references/snapshot-system.md` — title says "System Auto-Collect", labels are `[system:*]`, YAML key reference is `system:`
2. Review `SKILL.md` — all links point to `snapshot-system.md`, text says "system auto-collect" and "auto-collect system info", category order says `system` → `pyvenv`
3. Review `README.md` — line 23 says "Auto-collects system info"
4. Review `references/snapshot.md` — heading says "System (`system`)", link points to `snapshot-system.md`
5. Review `references/reproduce.md` — says "Skip `system` category" and "System-level info"
6. Review `assets/templates/env-snapshot-example.yaml` — top-level key is `system:`
7. Review `.vodka/env-snapshot-2026-02-27-20-56-46.yaml` — top-level key is `system:`
8. Run `grep -ri "server" --include="*.md" --include="*.yaml" --include="*.py"` excluding `.tequila/` — no hits in active source files (only the example hostname `dev-server` is acceptable)
9. Run `python3 scripts/print_yaml.py` — table shows `system` as the category

## Expected Outcome

All files use `system` instead of `server`. No stale `server` references remain in active source files. The print script outputs `system`.

## Result

- Status: PASS
- User confirmed all changes are correct
