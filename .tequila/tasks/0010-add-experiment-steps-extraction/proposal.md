# Proposal of *Add Experiment Steps Extraction*

## Motivation

When reproducing a development environment from a snapshot, users often need a quick reference of the actual experiment steps — the sequence of commands to run. Currently, the `:run` fields are scattered across multiple categories in the YAML snapshot, and users must manually read through the entire file to piece together the execution order. Extracting these into a standalone `experiment-steps.md` makes the reproduction workflow faster and less error-prone.

## Summary

- Parse a snapshot YAML and collect all `:run` field values from any category's named entries (`exec/<name>:run`, `script/<name>:run`, `container/<name>:run`, etc.)
- Preserve the order in which entries appear in the YAML
- Generate `.vodka/{snapshot-id}-{timestamp}/experiment-steps.md` with numbered steps
- The vodka skill reads the snapshot during the collect or reproduce flow and outputs the experiment steps file alongside the snapshot YAML

## Usage

```
Follow vodka skill, extract the experiment steps from {yaml}
```

## Impact

- Affected code: `SKILL.md` (skill instructions for step extraction), `references/reproduce.md` (link to experiment steps), snapshot subfolder (new `experiment-steps.md` output file)
