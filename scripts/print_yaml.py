#!/usr/bin/env python3
"""Print the latest .vodka/*/env-snapshot.yaml as a table."""

import glob
import os
import sys
import yaml


class FileTag:
    """Represents a !file tag value."""

    def __init__(self, path):
        self.path = path


def file_constructor(loader, node):
    return FileTag(loader.construct_scalar(node))


def make_loader():
    loader = yaml.SafeLoader
    loader.add_constructor("!file", file_constructor)
    return loader


def resolve_value(val, base_dir=".vodka"):
    """Resolve a value, reading file content if it's a !file reference."""
    if isinstance(val, FileTag):
        full_path = os.path.join(base_dir, val.path)
        if os.path.exists(full_path):
            with open(full_path) as f:
                return f.read().strip()
        return f"!file {val.path} (not found)"
    return val


def find_latest_snapshot():
    """Find the most recent snapshot subfolder by timestamp suffix."""
    files = sorted(glob.glob(".vodka/*/env-snapshot.yaml"))
    if not files:
        print("No snapshot files found in .vodka/*/", file=sys.stderr)
        sys.exit(1)
    return files[-1]


def load_snapshot(path):
    base_dir = os.path.dirname(path)
    with open(path) as f:
        data = yaml.load(f, Loader=make_loader())
    return data, base_dir


def print_table(data, base_dir=".vodka"):
    rows = []
    for category, fields in data.items():
        if isinstance(fields, dict):
            for key, value in fields.items():
                if isinstance(value, dict):
                    # Template category: category/name
                    for field, val in value.items():
                        resolved = resolve_value(val, base_dir)
                        rows.append((category, key, field, str(resolved)))
                elif isinstance(value, list):
                    rows.append((category, "", key, "\n".join(str(v) for v in value)))
                else:
                    resolved = resolve_value(value, base_dir)
                    rows.append((category, "", key, str(resolved)))

    headers = ("Category", "Name", "Field", "Value")
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            first_line = cell.split("\n")[0] if "\n" in cell else cell
            widths[i] = max(widths[i], len(first_line))

    def hline(left, mid, right, fill="─"):
        return left + mid.join(fill * (w + 2) for w in widths) + right

    def fmt(row):
        parts = []
        for i, cell in enumerate(row):
            first_line = cell.split("\n")[0] if "\n" in cell else cell
            parts.append(" " + first_line.ljust(widths[i]) + " ")
        return "│" + "│".join(parts) + "│"

    print(hline("┌", "┬", "┐"))
    print(fmt(headers))
    print(hline("├", "┼", "┤"))
    for idx, row in enumerate(rows):
        print(fmt(row))
        if "\n" in row[3]:
            for line in row[3].split("\n")[1:]:
                empty = ("", "", "", line)
                print(fmt(empty))
        if idx < len(rows) - 1:
            print(hline("├", "┼", "┤"))
    print(hline("└", "┴", "┘"))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else find_latest_snapshot()
    data, base_dir = load_snapshot(path)
    print_table(data, base_dir)


if __name__ == "__main__":
    main()
