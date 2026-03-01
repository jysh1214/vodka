# Python Manual Input

How to collect Python virtual environment information.

## Fields and Commands

| Field | Label | Command | Description |
|---|---|---|---|
| Module load | `[pyvenv/<name>:module]` | `module load python/3.11.5` | HPC module load command |
| Python version | `[pyvenv/<name>:version]` | `python3 --version` | Python interpreter version |
| Venv path | `[pyvenv/<name>:venv]` | `echo $VIRTUAL_ENV` | Virtual environment directory |
| Interpreter path | `[pyvenv/<name>:path]` | `which python3` | Full path to python3 binary |
| pip version | `[pyvenv/<name>:pip]` | `pip --version` | pip package manager version |
| Installed packages | `[pyvenv/<name>:packages]` | `pip freeze` | List of installed packages |

`<name>` is the virtual environment name from `python -m venv <name>`. Use `system` for system-wide Python.

## Collection Steps

1. User provides labeled input for each field (e.g., `[pyvenv/.venv:version] Python 3.11.5`)
2. For `[pyvenv/<name>:packages]`, save `pip freeze` output to `requirements-<name>.txt` in the snapshot subfolder and record the field as `packages: !file requirements-<name>.txt`
3. Store all fields under the `pyvenv:` → `<name>:` key in `.vodka/{snapshot-id}-{timestamp}/env-snapshot.yaml`
