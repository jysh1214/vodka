# Proposal of *Add Run Expect List Support*

## Motivation

Currently, the `run` field in template categories only supports a single string value. Users often need multiple sequential commands for an experiment (e.g., setting environment variables, running the binary, checking output). Additionally, there is no way to document expected validation checks alongside the run commands. Supporting YAML lists for `run` and adding an `expect` field enables users to capture complete experiment workflows with verification steps.

## Summary

- Support `run` as either a single string or a YAML list of commands
- Add an `expect` field (string or list) to template categories for validation checks
- Update `scripts/extract_steps.py` to handle list `run`/`expect` values and output checks attached to the last run step in each entry
- Update the exec template reference to document the new `expect` field and list syntax

## Usage

```
Follow vodka skill, extract the experiment steps from {yaml}
```

YAML input example:

```yaml
exec:
  firmware:
    run:
      - export LD_LIBRARY_PATH=/opt/libs
      - ./build/firmware.elf --config test.cfg
    expect:
      - diff output.bin expected.bin
      - test -f log.txt
```

Output `experiment-steps.md`:

```markdown
# steps:
1. export LD_LIBRARY_PATH=/opt/libs
2. ./build/firmware.elf --config test.cfg
   - check: diff output.bin expected.bin
   - check: test -f log.txt
```

## Impact

- Affected code: `scripts/extract_steps.py` (list handling + expect output), `references/snapshot-exec-template.md` (document expect field), `assets/templates/env-snapshot-example.yaml` (update example)
