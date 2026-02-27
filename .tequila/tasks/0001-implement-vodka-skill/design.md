# Design of *Implement Vodka Skill*

## Context

Vodka is a Claude Code skill that captures and organizes a complete snapshot of the user's development environment into a structured YAML file. It is prompt-driven — Claude Code reads the skill files and follows the defined workflow and rules to execute commands, collect input, and produce output. The repo currently contains only a LICENSE file; all skill files and references need to be created from scratch.

## Goals / Non-Goals

- Goals:
  - Create the full vodka skill file structure (`SKILL.md`, `README.md`, references)
  - Define auto-collect workflow for server and Python environment categories
  - Define manual input workflow for container, QEMU, toolchain, exec, and dep categories
  - Specify the labeled input format (`[category:field]` and `[category/name:field]`)
  - Specify the YAML output schema for `.vodka/env-snapshot.yaml`
- Non-goals:
  - Building a standalone CLI tool or script — this is a Claude Code skill (prompt-based)
  - Supporting non-YAML output formats in the initial implementation (JSON/Markdown table can be added later)
  - Automating container, QEMU, or toolchain detection — these are manual input categories

## Decisions

- Decision: Implement as a pure Claude Code skill (prompt files + reference docs, no scripts)
  - Rationale: Claude Code skills are prompt-driven. The skill files instruct Claude on what commands to run and how to structure output. No custom tooling is needed.
- Decision: Use a flat YAML structure grouped by category, with named sub-entries for multi-instance categories
  - Rationale: Keeps the snapshot file simple and human-readable while supporting multiple toolchains, execs, or deps.
- Decision: Place the category/field reference in `references/DEV_ENV_SNAPSHOT_CATEGORIES_FIELDS.md`
  - Rationale: Separates the reference data from the skill workflow, making both easier to maintain.

## Risks / Trade-Offs

- Some auto-collect commands may not be available on all systems (e.g., `module load`, `/etc/os-release` on non-Linux). The skill should handle missing commands gracefully by noting "N/A" or skipping the field.
- `pip freeze` can produce large output. The skill should include it as-is but could be truncated if it becomes unwieldy.

## Migration Plan

Not applicable — this is a greenfield implementation.
