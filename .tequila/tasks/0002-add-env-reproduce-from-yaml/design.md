# Design of *Add Env Reproduce from YAML*

## Context

Vodka can snapshot a dev environment into `.vodka/env-snapshot.yaml`. This task adds the reverse — the AI reads that YAML and reproduces the environment step by step, guided by `references/reproduce.md`.

## Goals / Non-Goals

- Goals:
  - Create `references/reproduce.md` that instructs the AI how to reproduce a dev environment from a snapshot YAML
  - Define priority order: `pyvenv` → `dep/*` or `deps/*` → others
  - Ensure the AI asks the user when it doesn't know how to handle a resource
  - Add reproduce workflow to `SKILL.md` and usage to `README.md`
- Non-goals:
  - Reproducing `server` fields (skipped entirely)
  - Using scripts — this is AI-guided, not script-driven

## Decisions

- Decision: AI-guided reproduce via reference doc instead of a script
  - Rationale: The AI can adapt to each environment, ask clarifying questions, and handle edge cases that a static script cannot.
- Decision: Priority order `pyvenv` → `dep/*` or `deps/*` → others
  - Rationale: Python environment is the foundation, dependencies come next, then everything else builds on top.
- Decision: Never guess — ask the user when unsure
  - Rationale: Guessing can lead to broken environments or security issues.

## Risks / Trade-Offs

- AI-guided approach depends on the AI correctly interpreting the reference doc each time. Clear, unambiguous instructions in `reproduce.md` mitigate this.
