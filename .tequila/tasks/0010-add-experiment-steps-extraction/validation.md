# Validation of *Add Experiment Steps Extraction*

## Validation Method

Run the script against the example YAML (which contains `exec/firmware:run`) and verify the output file content matches the expected format.

## Steps

1. Run `python3 scripts/extract_steps.py assets/templates/env-snapshot-example.yaml`
2. Check that `assets/templates/experiment-steps.md` was created
3. Verify its content is:
   ```
   # steps:
   1. ./build/firmware.elf
   ```
4. Clean up: `rm assets/templates/experiment-steps.md`
5. Run `python3 scripts/extract_steps.py` with no args against the current snapshot (which has no `run` fields) — should exit with error "No run fields found in snapshot."

## Expected Outcome

- Step 1: Script prints `Wrote assets/templates/experiment-steps.md`
- Step 3: File contains exactly the numbered step from the `exec/firmware:run` field
- Step 5: Script exits with code 1 and prints the error message

## Result

- Status: PASS
- Validated by user
