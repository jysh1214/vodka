# Subtasks of *Rename Server to System*

## File rename

- [x] Rename `references/snapshot-server.md` → `references/snapshot-system.md`

## Content updates

- [x] `references/snapshot-system.md` — update title, description, all `[server:*]` labels, and `server:` YAML key reference
- [x] `SKILL.md` — update link to `snapshot-system.md`, "server auto-collect" → "system auto-collect", "auto-collect server info" → "auto-collect system info" (×2), category order `server` → `system`
- [x] `README.md` — "Auto-collects server info" → "Auto-collects system info"
- [x] `references/snapshot.md` — "Server (`server`)" → "System (`system`)", link to `snapshot-system.md`
- [x] `references/reproduce.md` — "Skip `server` category" → "Skip `system` category", "Server-level info" → "System-level info"
- [x] `assets/templates/env-snapshot-example.yaml` — `server:` → `system:`
- [x] `.vodka/env-snapshot-2026-02-27-20-56-46.yaml` — `server:` → `system:`

## Verification

- [x] Grep active source files (excluding `.tequila/`) to confirm no remaining `server` references
- [x] Run `python3 scripts/print_yaml.py` to confirm table shows `system`
