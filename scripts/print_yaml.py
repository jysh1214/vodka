#!/usr/bin/env python3
"""Print .vodka/env-snapshot.yaml as a table."""

import sys
import yaml


def load_snapshot(path=".vodka/env-snapshot.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def print_table(data):
    rows = []
    for category, fields in data.items():
        if isinstance(fields, dict):
            for key, value in fields.items():
                if isinstance(value, dict):
                    # Template category: category/name
                    for field, val in value.items():
                        rows.append((category, key, field, str(val)))
                elif isinstance(value, list):
                    rows.append((category, "", key, "\n".join(str(v) for v in value)))
                else:
                    rows.append((category, "", key, str(value)))

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
