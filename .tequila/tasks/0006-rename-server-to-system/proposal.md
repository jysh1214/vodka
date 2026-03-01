# Proposal of *Rename Server to System*

## Motivation

The fields in this category (username, hostname, OS, kernel, architecture) describe any machine — local or remote. The term `server` implies a specific serving role, while `system` is a broader, more accurate name for what the category captures.

## Summary

- Rename `references/snapshot-server.md` → `references/snapshot-system.md` and update its content (title, description, labels, YAML key reference)
- Update `SKILL.md` references and category ordering rule from `server` to `system`
- Update `README.md` description from "server info" to "system info"
- Update `references/snapshot.md` category listing
- Update `references/reproduce.md` category references
- Update `assets/templates/env-snapshot-example.yaml` YAML key
- Update `.vodka/env-snapshot-2026-02-27-20-56-46.yaml` YAML key
- Leave `.tequila/tasks/` archived history unchanged

## Impact

- Affected code: `references/snapshot-server.md` (renamed), `SKILL.md`, `README.md`, `references/snapshot.md`, `references/reproduce.md`, `assets/templates/env-snapshot-example.yaml`, `.vodka/env-snapshot-*.yaml`
