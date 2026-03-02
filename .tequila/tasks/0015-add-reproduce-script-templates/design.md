# Design of *Add Reproduce Script Templates*

## Context

The reproduce workflow (`references/reproduce.md`) tells the skill what to generate but has no concrete examples. The skill must infer script structure each time, leading to inconsistent output. Adding templates based on the existing example YAML (`assets/templates/env-snapshot-example.yaml`) gives the skill a fixed reference.

## Goals / Non-Goals

- Goals:
  - Provide `assets/templates/reproduce.sh` as a reference for environment setup scripts
  - Provide `assets/templates/experiment-steps.sh` as a reference for exec section scripts
  - Provide `assets/templates/run_qemu.py` as a reference for QEMU pexpect interaction
  - Link templates from `references/reproduce.md` so the skill follows them
  - Templates should be based on the existing `env-snapshot-example.yaml` so the example is self-consistent

- Non-goals:
  - Making templates executable as-is (they are references, not runnable scripts)
  - Changing the reproduce workflow logic

## Decisions

- Decision: Use `#!/usr/bin/env bash` with `set -euo pipefail` as the standard header for shell templates.
  - This matches common practice for reproducible scripts.

- Decision: Use section comments (e.g., `# --- pyvenv: .venv ---`) to delimit categories in `reproduce.sh`.
  - Makes the generated script scannable and self-documenting.

- Decision: `run_qemu.py` template uses `pexpect.spawn()` with a timeout parameter and `pexpect.expect()` for validation.
  - Keeps the pattern simple and explicit.
