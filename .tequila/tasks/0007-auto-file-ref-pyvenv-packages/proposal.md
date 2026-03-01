# Proposal of *Auto File Ref Pyvenv Packages*

## Motivation

`pip freeze` output is always a multi-line package list — it never makes sense to inline it in the YAML. The `[pyvenv:packages]` field should always use `!file requirements.txt` automatically at snapshot time, instead of requiring a separate extraction step.

## Summary

- Update `references/snapshot-pyvenv.md` to instruct saving `pip freeze` output to `.vodka/requirements.txt` and using `!file requirements.txt` for the `packages` field
- Update `SKILL.md` workflow/rules if needed to reflect that `pyvenv:packages` always uses `!file`

## Impact

- Affected code: `references/snapshot-pyvenv.md`, possibly `SKILL.md`
