# Dependencies Template

Template for capturing arbitrary dependency information. Users can define any fields.

## Fields

| Field | Label | Example |
|---|---|---|
| (any) | `[dep/name:field]` | Any user-defined value |

## Example

```txt
[dep/openssl:version] 3.1.4
[dep/openssl:path] /usr/lib/x86_64-linux-gnu/libssl.so
[dep/openssl:checksum] md5sum:5a2b3c...
```
