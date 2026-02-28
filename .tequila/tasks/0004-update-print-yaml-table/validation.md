# Validation of *Update Print YAML Table*

## Validation Method

Run `python3 scripts/print_yaml.py` and visually confirm the output uses Unicode box-drawing characters with row separators between every row.

## Steps

1. Run `python3 scripts/print_yaml.py`
2. Verify the table uses `┌ ┬ ┐` for top border, `├ ┼ ┤` for row separators, `└ ┴ ┘` for bottom border, and `│` for column delimiters

## Expected Outcome

Table output with box-drawing borders matching the specified format, with separators between every data row.

## Result

- Status: PASS
- Output matches expected box-drawing format with all five server rows separated by `├──┼──┤` lines
