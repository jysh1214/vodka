# Subtasks of *Align YAML Order with Reproduce Priority*

## Implementation

- [x] Reorder `assets/templates/env-snapshot-example.yaml`: move `dep:` block right after `pyvenv:`
- [x] Reorder `references/snapshot.md`: move Dependencies before Container in the Templates list
- [x] Add a rule in `SKILL.md` requiring output YAML to always follow reproduction priority order: `server` → `pyvenv` → `dep`/`deps` → all others
- [x] Verify no other files reference a specific category order that needs updating
