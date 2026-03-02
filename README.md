# vodka

An AI skill that captures and organizes development environment into a structured YAML snapshot.

## Installation

Claude:

```txt
mkdir -p .claude/skills && git clone https://github.com/jysh1214/vodka.git .claude/skills/vodka && rm -rf .claude/skills/vodka/.git
```

Auggie:

```txt
mkdir -p .augment/skills && git clone https://github.com/jysh1214/vodka.git .augment/skills/vodka && rm -rf .augment/skills/vodka/.git
```

## Usage

### 1. Initial snapshot

Auto-collects system info and creates `.vodka/{snapshot-id}-{timestamp}/env-snapshot.yaml`:

```txt
Follow vodka skill, snapshot the development environment for {description}
```

Optionally include a Jira ticket ID:

```txt
Follow vodka skill, snapshot the development environment for {ticket} {description}
```

### 2. Add pyvenv snapshot (optional)

```txt
Follow vodka skill, snapshot pyvenv
```

### 3. Add any snapshots

Use labeled input with `[category/name:field] value`:

```txt
Follow vodka skill, add snapshot:
[category/name:field] value
[category/name:field] value
...
```

Multiple entries at the same time is okay. Adding entries creates a new folder with the same snapshot ID but a fresh timestamp.

### 4. Reproduce dev environment

Generates `reproduce.sh`, `experiment-steps.sh`, and optionally `run_qemu.py` into the snapshot subfolder:

```txt
Follow vodka skill, reproduce dev environment from {snapshot-id}
```

### 5. Extract large values to files

```txt
Follow vodka skill, extract large values to files
```

### 6. Show snapshot

```txt
Follow vodka skill, show snapshot
```
