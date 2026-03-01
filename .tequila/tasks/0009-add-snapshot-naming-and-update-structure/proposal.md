# Proposal of *Add Snapshot Naming and Update Structure*

## Motivation

Currently all snapshot files and `!file` references live flat in `.vodka/`. As snapshots accumulate, the folder becomes cluttered and there is no way to associate a snapshot with the experimental context that produced it. Organizing each snapshot into its own named subfolder ties the environment to a purpose (e.g., a Jira ticket or experiment description) and keeps related files together.

## Summary

- **BREAKING** — Change `.vodka/` from a flat directory to per-snapshot subfolders
- New folder structure: `.vodka/{ticket}-{snapshot-id}-{timestamp}/` or `.vodka/{snapshot-id}-{timestamp}/`
  - `env-snapshot.yaml` — the snapshot file (no longer needs a timestamp in the filename)
  - `requirements-{pyvenv/name}.txt` — `!file` references stored alongside the snapshot
- Snapshot IDs use a kebab-case, verb-led descriptive phrase, optionally prefixed with a Jira ticket ID
  - Examples: `PROJ-123-benchmark-inference-latency`, `COMP-5566-optimize-model-quantization`, `profile-memory-usage`
  - Prefer verb prefixes: `benchmark-`, `optimize-`, `profile-`, `tune-`, `test-`, etc.
- When adding new entries to an existing snapshot, create a new folder with the same `{ticket}-{snapshot-id}` but a fresh `{timestamp}`. The new folder contains a complete merged snapshot. This preserves snapshot history while keeping the same context identity.
  - Example: initial `.vodka/PROJ-123-benchmark-inference-latency-2026-03-01-07-09-11/` → after adding pyvenv `.vodka/PROJ-123-benchmark-inference-latency-2026-03-01-08-15-30/`
- Update usage to: "Follow vodka skill, snapshot the development environment for {description}" (optionally with a Jira ticket ID)
- Update `SKILL.md` workflow, rules, and file path references
- Update `README.md` usage examples
- Update `references/snapshot-system.md`, `references/snapshot-pyvenv.md`, `references/file-reference.md` path references
- Update `scripts/print_yaml.py` to find the latest snapshot subfolder
- Migrate existing `.vodka/` contents to the new structure

## Impact

- Affected code: `SKILL.md`, `README.md`, `references/snapshot-system.md`, `references/snapshot-pyvenv.md`, `references/file-reference.md`, `scripts/print_yaml.py`, `.vodka/`
