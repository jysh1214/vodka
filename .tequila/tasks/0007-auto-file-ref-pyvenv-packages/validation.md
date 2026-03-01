# Validation of *Auto File Ref Pyvenv Packages*

## Validation Method

Manual review of `references/snapshot-pyvenv.md` to confirm the `[pyvenv:packages]` collection step uses `!file requirements.txt` and is consistent with `references/file-reference.md`.

## Steps

1. Review `references/snapshot-pyvenv.md` step 2 — should instruct saving `pip freeze` output to `.vodka/requirements.txt` and recording `packages: !file requirements.txt`
2. Confirm the `!file` path format is consistent with `references/file-reference.md` (paths relative to `.vodka/`)

## Expected Outcome

Step 2 clearly instructs always using `!file requirements.txt` for the packages field. No ambiguity about whether to inline or extract.

## Result

- Status: PASS
- User confirmed all changes are correct
