# Subtasks of *Add Reproduce Target Directory*

## Update reproduce.md

- [x] Add a "Target Directory" section explaining the optional target directory parameter and its behavior
- [x] Update pyvenv step: when target is provided, create venv at `<target>/<name>` using the Python resolved after any `module load`, then activate and install packages
- [x] Update pyvenv step: when target is not provided, keep existing behavior (use `venv` field or system Python)
- [x] Update SKILL.md workflow step 6 to mention the target directory option
