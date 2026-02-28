# Proposal of *Update Print YAML Table*

## Motivation

The current `scripts/print_yaml.py` outputs a plain ASCII table using `|` and `-` characters. This is functional but visually plain. Switching to Unicode box-drawing characters (`┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘ │ ─`) produces a cleaner, more professional table that is easier to read in the terminal.

## Summary

- Replace the `print_table` function in `scripts/print_yaml.py` to use Unicode box-drawing characters
- Render horizontal separators between every row (not just after the header)
- Use `┌ ┐ └ ┘` for corners, `├ ┤` for row separators, `┬ ┴ ┼` for column intersections, `─` for horizontal lines, and `│` for vertical lines
- Keep multi-line value handling (continuation lines for fields like package lists)
- No new dependencies — use only Python stdlib

## Impact

- Affected code: `scripts/print_yaml.py` (`print_table` function)
