#!/usr/bin/env python3
"""Extract experiment steps (run fields) from a snapshot YAML."""

import os
import sys

from print_yaml import find_latest_snapshot, load_snapshot

SKIP_CATEGORIES = {"system", "pyvenv"}


def as_list(val):
    """Normalize a string or list value into a list."""
    if isinstance(val, list):
        return [str(v) for v in val]
    if isinstance(val, str):
        return [val]
    return []


def extract_run_fields(data):
    """Collect (run_commands, expect_checks) from template categories in document order."""
    entries = []
    for category, cat_entries in data.items():
        if category in SKIP_CATEGORIES:
            continue
        if not isinstance(cat_entries, dict):
            continue
        for name, fields in cat_entries.items():
            if not isinstance(fields, dict):
                continue
            if "run" in fields:
                runs = as_list(fields["run"])
                expects = as_list(fields.get("expect", "exit code 0"))
                if runs:
                    entries.append((runs, expects))
    return entries


def write_steps(entries, base_dir):
    out_path = os.path.join(base_dir, "experiment-steps.md")
    with open(out_path, "w") as f:
        f.write("# steps:\n")
        step_num = 1
        for runs, expects in entries:
            for j, cmd in enumerate(runs):
                f.write(f"{step_num}. {cmd}\n")
                if j == len(runs) - 1:
                    for chk in expects:
                        f.write(f"   - check: {chk}\n")
                step_num += 1
    print(f"Wrote {out_path}")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else find_latest_snapshot()
    data, base_dir = load_snapshot(path)
    entries = extract_run_fields(data)
    if not entries:
        print("No run fields found in snapshot.", file=sys.stderr)
        sys.exit(1)
    write_steps(entries, base_dir)


if __name__ == "__main__":
    main()
