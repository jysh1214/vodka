# Proposal of *Implement Vodka Skill*

## Motivation

Developers need a quick, reproducible way to capture their full development environment — server info, Python setup, containers, toolchains, QEMU config, and custom dependencies — so that environments can be documented, shared, and reconstructed. Currently there is no structured mechanism to snapshot this information. The vodka skill automates auto-collectable fields and provides a labeled input format for manual entries, producing a single `.vodka/env-snapshot.yaml` file.

## Summary

- Implement the vodka Claude Code skill that captures dev environment snapshots
- Auto-collect server info (`whoami`, `hostname`, `uname`, `os-release`) and Python environment info (`python3 --version`, `pip freeze`, `$VIRTUAL_ENV`, etc.) on first invocation
- Accept manual labeled input in `[category:field] value` and `[category/name:field] value` format for container, QEMU, toolchain, executable, and dependency categories
- Merge and deduplicate entries; group multi-entry categories by name
- Output structured YAML to `.vodka/env-snapshot.yaml` (with optional JSON/Markdown table on request)
- Support incremental snapshots — users can add entries at any time and the file is updated in place

## Impact

- Affected code: `SKILL.md` (skill entrypoint), `references/DEV_ENV_SNAPSHOT_CATEGORIES_FIELDS.md` (category/field reference), `.vodka/env-snapshot.yaml` (generated output)
- New directory: `.vodka/` created at project root on first snapshot
