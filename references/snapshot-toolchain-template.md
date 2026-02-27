# Toolchain Template

Template for capturing toolchain environment information.

## Fields

| Field | Label | Example |
|---|---|---|
| Module load | `[toolchain/name:module]` | `module load gcc/13.2.0` |
| Name | `[toolchain/name:name]` | `arm-none-eabi-gcc` |
| Package path | `[toolchain/name:path]` | `/usr/local/bin/arm-none-eabi-gcc` |
| Version | `[toolchain/name:version]` | `13.2.0` |
| Binary checksum | `[toolchain/name:checksum]` | `md5sum:9c1d4e...` |

## Example

```txt
[toolchain/arm-gcc:module] module load gcc/13.2.0
[toolchain/arm-gcc:name] arm-none-eabi-gcc
[toolchain/arm-gcc:path] /usr/local/bin/arm-none-eabi-gcc
[toolchain/arm-gcc:version] 13.2.0
[toolchain/arm-gcc:checksum] md5sum:9c1d4e...
```
