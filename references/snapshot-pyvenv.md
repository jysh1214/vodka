# Python Manual Input

How to collect Python virtual environment information.

## Fields and Commands

| Field | Label | Command | Description |
|---|---|---|---|
| Module load | `[pyvenv:module]` | `module load python/3.11.5` | HPC module load command |
| Python version | `[pyvenv:version]` | `python3 --version` | Python interpreter version |
| Venv path | `[pyvenv:venv]` | `echo $VIRTUAL_ENV` | Virtual environment directory |
| Interpreter path | `[pyvenv:path]` | `which python3` | Full path to python3 binary |
| pip version | `[pyvenv:pip]` | `pip --version` | pip package manager version |
| Installed packages | `[pyvenv:packages]` | `pip freeze` | List of installed packages |

## Collection Steps

1. User provides labeled input for each field (e.g., `[pyvenv:version] Python 3.11.5`)
2. For `[pyvenv:packages]`, accept a multi-line list of packages in `pip freeze` format
3. Store all fields under the `pyvenv:` key in `.vodka/env-snapshot.yaml`
