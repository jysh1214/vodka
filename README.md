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

Auto-collects server info and creates `.vodka/env-snapshot.yaml`:

```txt
Follow vodka skill, snapshot development environment
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

Multiple entries at the same time is okay.

### 4. Reproduce dev environment

```txt
Follow vodka skill, reproduce dev environment from {yaml}
```

### 5. Extract large values to files

```txt
Follow vodka skill, extract large values to files
```

### 6. Show snapshot

```txt
Follow vodka skill, show snapshot
```

## File References

Large values can be stored in separate files using the `!file` tag:

```yaml
pyvenv:
  packages: !file requirements.txt
```

## Output

Snapshot is saved to `.vodka/env-snapshot.yaml`.
