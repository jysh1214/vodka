#!/usr/bin/env python3
"""run_qemu.py — Run QEMU interactive commands using pexpect.

Generated from: env-snapshot.yaml
"""

import sys
import pexpect

TIMEOUT = 60


def run_qemu():
    # Spawn QEMU process with the startup command
    child = pexpect.spawn(
        "qemu-system-arm -M stm32 -kernel firmware.bin",
        timeout=TIMEOUT,
        encoding="utf-8",
    )

    # Send additional commands from run field (if any)
    child.sendline("command_1")
    child.sendline("command_2")

    # Validate expect fields
    child.expect("expected_output_pattern_1")
    child.expect("expected_output_pattern_2")

    child.close()
    if child.exitstatus != 0:
        print(f"QEMU exited with status {child.exitstatus}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    run_qemu()
