# Proposal of *Add Reproduce Script Templates*

## Motivation

The reproduce workflow in `references/reproduce.md` describes *what* the skill should generate (`reproduce.sh`, `experiment-steps.sh`, `run_qemu.py`) but provides no example output. This means the AI skill interprets the instructions differently each time, leading to inconsistent script structure, variable naming, and error handling across runs. Adding concrete templates gives the skill a reference to follow, producing predictable and uniform scripts.

## Summary

- Add `assets/templates/reproduce.sh` — template showing the expected structure for environment setup scripts (pyvenv, deps, other categories)
- Add `assets/templates/experiment-steps.sh` — template showing the expected structure for exec section scripts
- Add `assets/templates/run_qemu.py` — template showing the expected pexpect pattern for QEMU interactive commands
- Reference the templates from `references/reproduce.md` so the skill uses them as a basis when generating scripts

## Impact

- Affected code: `assets/templates/` (3 new files), `references/reproduce.md` (add template references)
