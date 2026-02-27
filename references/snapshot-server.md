# Server Auto-Collect

How to collect server information automatically.

## Fields and Commands

| Field | Label | Command | Description |
|---|---|---|---|
| Username | `[server:user]` | `whoami` | Current logged-in user |
| Hostname | `[server:hostname]` | `hostname` | Machine hostname |
| OS name/version | `[server:os]` | `cat /etc/os-release` | OS distribution and version |
| Kernel | `[server:kernel]` | `uname -r` | Kernel version string |
| Architecture | `[server:arch]` | `uname -m` | CPU architecture (e.g., x86_64, aarch64) |

## Collection Steps

1. Run each command in the table above
2. If a command fails or is unavailable, record the field value as `N/A`
3. For `cat /etc/os-release`, extract the `PRETTY_NAME` value for a concise OS description
4. Store all fields under the `server:` key in `.vodka/env-snapshot.yaml`
