# Validation of *Add Run Expect List Support*

## Validation Method

Run the script against three cases: list run + expect, single string run + expect, and run without expect (default check).

## Steps

1. Run `python3 scripts/extract_steps.py assets/templates/env-snapshot-example.yaml` (list run + list expect)
2. Verify `assets/templates/experiment-steps.md` contains:
   ```
   # steps:
   1. export LD_LIBRARY_PATH=/opt/libs
   2. ./build/firmware.elf --config test.cfg
      - check: diff output.bin expected.bin
      - check: test -f log.txt
   ```
3. Clean up: `rm assets/templates/experiment-steps.md`
4. Create a temp YAML with single string `run` and no `expect`, run the script, verify output has `- check: exit code 0`
5. Verify backward compatibility: single string `run` still works

## Expected Outcome

- List run + list expect: checks attached to last run step
- No expect: defaults to `- check: exit code 0`
- Single string run: treated as one-element list, works as before

## Result

- Status: PASS
- Validated by user
