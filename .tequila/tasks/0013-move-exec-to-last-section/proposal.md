# Proposal of *Move Exec to Last Section*

## Motivation

The `exec` category represents runtime execution steps that depend on all other categories (system, pyvenv, deps, containers, toolchains, etc.) being set up first. The current ordering rule (`system → pyvenv → dep/deps → all others`) treats `exec` the same as any other category, but it should always come last to reflect the actual reproduction order.

## Summary

- Update the category ordering rule in `SKILL.md` to place `exec` always last: `system → pyvenv → dep/deps → all others → exec`
- Update `references/reproduce.md` priority order to list `exec` as the final step
- Update `references/snapshot.md` if it documents category ordering

## Impact

- Affected code: `SKILL.md` (Rules section), `references/reproduce.md` (Priority Order section), `references/snapshot.md`
