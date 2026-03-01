# Design of *Add Experiment Steps Extraction*

## Context

The vodka skill captures dev environment snapshots as YAML. Template categories (`exec`, `container`, `qemu`, `toolchain`, and any user-defined category) can have a `run` field that holds an execution command. Currently there is no way to extract these into a standalone runnable list. Users must manually scan the YAML to reconstruct the experiment sequence.

## Goals / Non-Goals

- Goals: Extract all `:run` fields from a snapshot YAML in document order and write them as numbered steps to `experiment-steps.md`
- Non-goals: Auto-executing the steps, modifying the snapshot YAML, handling fields other than `run`

## Decisions

- Decision: Add a Python script `scripts/extract_steps.py` that parses the snapshot YAML and generates the `experiment-steps.md` file. Reuse the existing YAML loading utilities from `scripts/print_yaml.py` (`FileTag`, `file_constructor`, `make_loader`, `find_latest_snapshot`, `load_snapshot`).
- Alternatives considered: LLM-based extraction (skill reads YAML and writes the file). Rejected because a script is deterministic, reproducible, and can be run independently without the skill.

- Decision: Scan all categories except `system` and `pyvenv` for `run` fields. `system` has no named entries, and `pyvenv` has no `run` field by convention.
- Alternatives considered: Only scanning `exec`. Rejected because any template category can have a `run` field.

- Decision: Output format uses a flat numbered list under a `# steps:` heading, matching the user's specification.

## Risks / Trade-Offs

- If a snapshot has no `run` fields, no `experiment-steps.md` is generated. The skill should inform the user.
- Document order dependency: YAML key order is preserved in the snapshot (as written by the skill), so extraction order is deterministic.
