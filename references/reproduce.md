# Reproduce Dev Environment from Snapshot

Generate shell scripts to reproduce a development environment from a snapshot YAML.

## Usage

```
Follow vodka skill, reproduce dev environment from {snapshot-id}
```

The skill locates the latest snapshot subfolder matching `{snapshot-id}` under `.vodka/`, reads its `env-snapshot.yaml`, and generates scripts into that same subfolder.

## Rules

- Skip `system` category entirely. System-level info is not reproducible.
- If you do not know how to obtain, compile, build, or install a resource, ask the user. Do not guess.
- If a field value uses `!file path`, read the referenced file from the snapshot subfolder to get the actual value and inline it into the generated script.

## Output Scripts

The skill generates the following scripts into `.vodka/{snapshot-id}-{timestamp}/`:

### 1. reproduce.sh

Template: [assets/templates/reproduce.sh](../assets/templates/reproduce.sh)

Covers all categories **except** `exec` and `system`, in priority order:

1. `pyvenv/*` — Python virtual environments
2. `dep/*` or `deps/*` — Dependencies
3. All other categories (container, qemu, toolchain, etc.)

Within the same category, follow the order as they appear in the YAML.

#### pyvenv/*

For each named Python environment (where `<name>` is the key under `pyvenv`):

1. If `module` field exists, emit the `module load` command.
2. Emit `python3 -m venv <name>` and `source <name>/bin/activate`.
3. If `packages` field exists, emit `pip install <package1> <package2> ...`

#### dep/* or deps/*

For each named dependency:

1. If `module` field exists, emit the `module load` command.
2. For other fields (version, path, checksum, etc.), emit commands to verify or install the dependency.
3. If you do not know how to install the dependency, ask the user for instructions.

#### Other categories

For each remaining category (container, qemu, toolchain, etc.) excluding `exec`:

1. If `module` field exists, emit the `module load` command.
2. If `startup` field exists, emit it as the setup command.
3. If `build` field exists, emit it as the build command.
4. If you do not know how to set up the resource, ask the user.

### 2. experiment-steps.sh

Template: [assets/templates/experiment-steps.sh](../assets/templates/experiment-steps.sh)

Covers the `exec` section only. Execution steps run after all environments and dependencies are ready.

For each named exec entry:

1. If `cd` field exists, emit `cd <cd value>`.
2. If `build` field exists, emit it as the build command.
3. If `run` field exists (string or list), emit each command in order.
4. If `expect` field exists (string or list), emit each check as a validation command after the run commands.
5. If `startup` field exists, emit it as the launch command.
6. If an exec entry involves QEMU (its commands contain `qemu`, case-insensitive), emit `python3 run_qemu.py` instead of the raw commands. See `run_qemu.py` below.

### 3. run_qemu.py (optional)

Template: [assets/templates/run_qemu.py](../assets/templates/run_qemu.py)

Generated only when `exec` entries involve QEMU commands. Uses `pexpect` to spawn and interact with QEMU processes.

**Important:** Refer to YAML comments in the QEMU section for interaction guidance (e.g., expected prompts, wait patterns, timeouts, send sequences). Use these comments to shape the pexpect logic.

For each QEMU exec entry, the script:

1. Spawns the QEMU process using `pexpect.spawn()` with the `startup` or `run` command.
2. Sends any additional commands from `run` (if a list) as interactive input.
3. Validates `expect` fields using `pexpect.expect()`.

`experiment-steps.sh` calls `python3 run_qemu.py` for QEMU steps.

## Notification

After generating the scripts, inform the user:

- `reproduce.sh`, `experiment-steps.sh`, and optionally `run_qemu.py` have been generated in `.vodka/{snapshot-id}-{timestamp}/`
- Users can copy these scripts to their target directory and run them to reproduce the environment and experiments
