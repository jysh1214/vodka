# Validation of *Align YAML Order with Reproduce Priority*

## Validation Method

Review all modified files to confirm categories are listed in reproduction priority order: `server` → `pyvenv` → `dep`/`deps` → all others.

## Steps

1. Check `assets/templates/env-snapshot-example.yaml` — `dep:` should appear right after `pyvenv:`
2. Check `references/snapshot.md` — Dependencies should be first in the Templates list
3. Check `SKILL.md` — reference list should have dep template before container; rules should include the category ordering requirement

## Expected Outcome

All files list categories in reproduction priority order, and SKILL.md includes a rule enforcing this order on output YAML.

## Result

- Status: PASS
- All three files updated with correct category ordering; SKILL.md rule guarantees order regardless of input order
