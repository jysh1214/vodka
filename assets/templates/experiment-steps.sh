#!/usr/bin/env bash
set -euo pipefail

# experiment-steps.sh — Execution steps (exec section only)
# Generated from: env-snapshot.yaml
# Run this after reproduce.sh has set up the environment.

# --- exec: firmware ---
make -j4
export LD_LIBRARY_PATH=/opt/libs
./build/firmware.elf --config test.cfg
# checks:
diff output.bin expected.bin
test -f log.txt

# --- exec: qemu-firmware (QEMU example) ---
# This entry involves QEMU; delegate to run_qemu.py
python3 run_qemu.py
