# Subtasks of *Add Experiment Steps Extraction*

## Script

- [x] Create `scripts/extract_steps.py`: parse snapshot YAML, collect `run` fields from all categories (except `system`, `pyvenv`) in document order, write `experiment-steps.md` to the snapshot subfolder

## Skill Integration

- [x] Add workflow step 7 to `SKILL.md`: if users want to extract experiment steps, run `python3 scripts/extract_steps.py`
