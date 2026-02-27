# QEMU Template

Template for capturing QEMU emulator environment information.

## Fields

| Field | Label | Example |
|---|---|---|
| Module load | `[qemu/name:module]` | `module load qemu/8.2.0` |
| Package path | `[qemu/name:path]` | `/usr/bin/qemu-system-arm` |
| Version | `[qemu/name:version]` | `8.2.0` |
| Binary checksum | `[qemu/name:checksum]` | `md5sum:a3f8b2c...` |
| Startup command | `[qemu/name:startup]` | `qemu-system-arm -M stm32 -kernel firmware.bin` |

## Example

```txt
[qemu/stm32:module] module load qemu/8.2.0
[qemu/stm32:path] /usr/bin/qemu-system-arm
[qemu/stm32:version] 8.2.0
[qemu/stm32:checksum] md5sum:a3f8b2c...
[qemu/stm32:startup] qemu-system-arm -M stm32 -kernel firmware.bin
```
