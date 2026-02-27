#!/usr/bin/env python3
"""Print .vodka/env-snapshot.yaml as a table."""

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


def load_snapshot(path=".vodka/env-snapshot.yaml"):
    with open(path) as f:
        return yaml.load(f, Loader=make_loader())


def print_table(data):
    rows = []
    for category, fields in data.items():
        if isinstance(fields, dict):
            for key, value in fields.items():
                if isinstance(value, dict):
                    # Template category: category/name
                    for field, val in value.items():
                        resolved = resolve_value(val)
                        rows.append((category, key, field, str(resolved)))
                elif isinstance(value, list):
                    rows.append((category, "", key, "\n".join(str(v) for v in value)))
                else:
                    resolved = resolve_value(value)
                    rows.append((category, "", key, str(resolved)))

    headers = ("Category", "Name", "Field", "Value")
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            first_line = cell.split("\n")[0] if "\n" in cell else cell
            widths[i] = max(widths[i], len(first_line))

    def fmt(row):
        parts = []
        for i, cell in enumerate(row):
            first_line = cell.split("\n")[0] if "\n" in cell else cell
            parts.append(first_line.ljust(widths[i]))
        return "| " + " | ".join(parts) + " |"

    sep = "|-" + "-|-".join("-" * w for w in widths) + "-|"

    print(fmt(headers))
    print(sep)
    for row in rows:
        print(fmt(row))
        if "\n" in row[3]:
            for line in row[3].split("\n")[1:]:
                padding = "| " + " | ".join("".ljust(widths[i]) for i in range(3))
                print(f"{padding} | {line.ljust(widths[3])} |")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else ".vodka/env-snapshot.yaml"
    data = load_snapshot(path)
    print_table(data)


if __name__ == "__main__":
    main()
