# Design of *Update Print YAML Table*

## Context

`scripts/print_yaml.py` has a `print_table` function (lines 52–91) that renders snapshot data using plain ASCII (`|`, `-`). The goal is to replace it with Unicode box-drawing output while keeping the same row-building logic and multi-line value support.

## Goals / Non-Goals

- Goals: Replace ASCII table borders with Unicode box-drawing characters; add row separators between every data row
- Non-goals: Changing the data-gathering logic, adding color/styling, or adding external dependencies

## Decisions

- Decision: Rewrite only the rendering portion of `print_table` (line formatting and separator helpers). The row-collection loop (lines 53–66) stays unchanged.
- Decision: Use three separator helpers — `top_border` (`┌─┬─┐`), `mid_separator` (`├─┼─┤`), and `bottom_border` (`└─┴─┘`) — built from column widths.
- Decision: Format data/header rows with `│` delimiters instead of `|`.
- Decision: Multi-line continuation lines use `│` delimiters with empty left columns, same as today but with box-drawing characters.
- Alternatives considered: Using a library like `rich` or `tabulate` — rejected to keep zero external dependencies beyond PyYAML.

## Risks / Trade-Offs

- Terminals without Unicode support will show garbled output. This is acceptable since virtually all modern terminals support Unicode.
