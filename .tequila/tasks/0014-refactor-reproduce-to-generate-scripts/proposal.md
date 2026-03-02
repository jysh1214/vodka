# Proposal of *Refactor Reproduce to Generate Scripts*

## Motivation

The current reproduce workflow runs commands interactively inside a user-specified `{target}` directory. This couples the skill to live execution and makes it hard to rerun experiments later. Users need portable, self-contained scripts they can place in any directory and execute independently. Removing the `{target}` parameter simplifies the usage and shifts responsibility for where scripts run to the user.

## Summary

- **BREAKING** Remove the `{target}` directory parameter from the reproduce workflow. New usage: `Follow vodka skill, reproduce dev environment from {snapshot-id}`
- The skill locates the latest snapshot subfolder matching `{snapshot-id}` under `.vodka/`, reads its `env-snapshot.yaml`, and generates scripts into that same subfolder
- Generate `reproduce.sh` from the YAML snapshot, covering all categories **except** the `exec` section (pyvenv, dep/deps, container, qemu, toolchain, etc.)
- Generate `experiment-steps.sh` from the `exec` section only
- If the `exec` section includes QEMU entries, generate `run_qemu.py` (using `pexpect`) to handle QEMU interactive commands; `experiment-steps.sh` will call `run_qemu.py`
- Notify the user that `reproduce.sh`, `experiment-steps.sh`, and optionally `run_qemu.py` are generated in `.vodka/{snapshot-id}-{timestamp}/` and ready to use

## Impact

- Affected code: `SKILL.md` (workflow step 6, usage wording), `references/reproduce.md` (rewrite to script-generation flow)
