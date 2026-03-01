# Design of *Align YAML Order with Reproduce Priority*

## Context

The reproduction priority (`references/reproduce.md`) is: `pyvenv` → `dep/*` → all others. The example template and snapshot reference list `dep` last, after container, qemu, toolchain, and exec.

## Goals / Non-Goals

- Goals: Reorder categories in the example template and reference doc to match reproduction priority; add a rule in `SKILL.md` to guarantee output YAML always follows this order regardless of input order
- Non-goals: Changing the reproduction logic itself, reordering fields within a category

## Decisions

- Decision: Target order is `server`, `pyvenv`, `dep`, then remaining templates (container, qemu, toolchain, exec)
- Decision: In `references/snapshot.md`, move Dependencies before Container in the Templates list
- Decision: In `assets/templates/env-snapshot-example.yaml`, move the `dep:` block right after `pyvenv:`
- Decision: Add a rule in `SKILL.md` requiring categories to be written in reproduction priority order: `server` → `pyvenv` → `dep`/`deps` → all others
- Decision: The existing `.vodka/env-snapshot-*.yaml` only has `server`, so no reorder needed
