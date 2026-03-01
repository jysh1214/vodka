# Executable Binaries Template

Template for capturing executable binary information.

## Fields

| Field | Label | Example |
|---|---|---|
| Name | `[exec/name:name]` | `firmware.elf` |
| Build command | `[exec/name:build]` | `make -j4` |
| Execution command | `[exec/name:run]` | `./build/firmware.elf` (string or list) |
| Validation check | `[exec/name:expect]` | `diff output.bin expected.bin` (string or list) |
| Binary checksum | `[exec/name:checksum]` | `md5sum:7b2e1f...` |

## Example

```txt
[exec/firmware:name] firmware.elf
[exec/firmware:build] make -j4
[exec/firmware:run] ./build/firmware.elf
[exec/firmware:expect] diff output.bin expected.bin
[exec/firmware:checksum] md5sum:7b2e1f...
```
