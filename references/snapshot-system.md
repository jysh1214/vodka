# System Auto-Collect

How to collect system information automatically.

## Fields and Commands

| Field | Label | Command | Description |
|---|---|---|---|
| Username | `[system:user]` | `whoami` | Current logged-in user |
| Hostname | `[system:hostname]` | `hostname` | Machine hostname |
| OS name/version | `[system:os]` | `cat /etc/os-release` | OS distribution and version |
| Kernel | `[system:kernel]` | `uname -r` | Kernel version string |
| Architecture | `[system:arch]` | `uname -m` | CPU architecture (e.g., x86_64, aarch64) |

## Collection Steps

1. Run each command in the table above
2. If a command fails or is unavailable, record the field value as `N/A`
3. For `cat /etc/os-release`, extract the `PRETTY_NAME` value for a concise OS description
4. Store all fields under the `system:` key in `.vodka/env-snapshot-{YYYY-MM-DD-HH-MM-SS}.yaml`
