# Proposal of *Add Env Reproduce from YAML*

## Motivation

Vodka currently captures dev environment snapshots into `.vodka/env-snapshot.yaml`, but there is no way to reproduce an environment from that YAML. Users need the reverse workflow — given a snapshot YAML, vodka should be able to guide or execute the steps to recreate the same dev environment on a new machine or session.

## Summary

- Add a "reproduce" workflow to vodka guided by `references/reproduce.md`
- Skip `server` fields (server-level info is not reproducible)
- Follow priority order: `pyvenv` → `dep/*` or `deps/*` → others
- If the AI does not know how to obtain, compile, build, or install a resource, it should ask the user. Do not guess.
- Update `SKILL.md` and `README.md` with the new reproduce workflow

## Impact

- Affected code: `SKILL.md`, `README.md`, `references/reproduce.md` (new reference)
- No breaking changes to existing snapshot workflow
