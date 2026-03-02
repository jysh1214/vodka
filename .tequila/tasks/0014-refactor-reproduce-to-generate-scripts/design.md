# Design of *Refactor Reproduce to Generate Scripts*

## Context

The vodka skill's reproduce workflow currently operates interactively: the user provides a `{yaml}` and `{target}`, and the skill runs setup commands live inside the target directory. This is tightly coupled and not rerunnable. The goal is to generate self-contained shell scripts that users can place anywhere and execute independently.

The skill already has `scripts/extract_steps.py` which extracts `run`/`expect` fields into `experiment-steps.md`. This task replaces that markdown output with executable `.sh` scripts and adds QEMU-specific `pexpect` handling.

## Goals / Non-Goals

- Goals:
  - Generate `reproduce.sh` covering all categories except `exec` (and `system`, which is already skipped)
  - Generate `experiment-steps.sh` covering the `exec` section only
  - Generate `run_qemu.py` when QEMU entries exist in `exec`, using `pexpect` for interactive commands
  - Remove the `{target}` parameter — new usage takes `{snapshot-id}` instead
  - Output scripts to the snapshot subfolder (`.vodka/{snapshot-id}-{timestamp}/`) alongside `env-snapshot.yaml`

- Non-goals:
  - Executing the generated scripts (users run them manually)
  - Handling `system` category (remains skipped as before)
  - Changing the snapshot collection workflow

## Decisions

- Decision: Rewrite `references/reproduce.md` from an interactive execution guide to a script-generation guide.
  - The document will describe what each generated script contains and how the skill produces them.

- Decision: Generate scripts into the snapshot subfolder (`.vodka/{snapshot-id}-{timestamp}/`, same directory as `env-snapshot.yaml`).
  - The skill locates the latest subfolder matching the given `{snapshot-id}` and writes scripts there.

- Decision: Detect QEMU in `exec` by checking if any exec entry's `run` or `startup` commands contain `qemu` (case-insensitive), or if the category path includes `qemu`.
  - Alternative considered: require explicit annotation in YAML. Rejected — adds user burden for something detectable automatically.

- Decision: `run_qemu.py` uses `pexpect` to spawn and interact with QEMU processes.
  - `experiment-steps.sh` calls `python3 run_qemu.py` for QEMU steps instead of running them directly.

## Risks / Trade-Offs

- Risk: `!file` references in YAML values need resolving at generation time. Mitigation: the skill already reads `!file` references during reproduce — same logic applies when building script content.
- Trade-off: Generated scripts are static snapshots of the YAML content. If the YAML changes, scripts must be regenerated. This is acceptable since snapshots are immutable by convention.
