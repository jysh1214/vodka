#!/usr/bin/env python3
"""Extract experiment steps (run fields) from a snapshot YAML."""

import os
import sys

from print_yaml import find_latest_snapshot, load_snapshot

SKIP_CATEGORIES = {"system", "pyvenv"}


def extract_run_fields(data):
    """Collect all run field values from template categories in document order."""
    steps = []
    for category, entries in data.items():
        if category in SKIP_CATEGORIES:
            continue
        if not isinstance(entries, dict):
            continue
        for name, fields in entries.items():
            if not isinstance(fields, dict):
                continue
            if "run" in fields:
                val = fields["run"]
                if isinstance(val, str):
                    steps.append(val)
    return steps


def write_steps(steps, base_dir):
    out_path = os.path.join(base_dir, "experiment-steps.md")
    with open(out_path, "w") as f:
        f.write("# steps:\n")
        for i, step in enumerate(steps, 1):
            f.write(f"{i}. {step}\n")
    print(f"Wrote {out_path}")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else find_latest_snapshot()
    data, base_dir = load_snapshot(path)
    steps = extract_run_fields(data)
    if not steps:
        print("No run fields found in snapshot.", file=sys.stderr)
        sys.exit(1)
    write_steps(steps, base_dir)


if __name__ == "__main__":
    main()
