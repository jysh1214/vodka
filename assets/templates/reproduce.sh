#!/usr/bin/env bash
set -euo pipefail

# reproduce.sh — Environment setup (all categories except exec and system)
# Generated from: env-snapshot.yaml

# --- pyvenv: .venv ---
module load python/3.11.5
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-.venv.txt

# --- dep: openssl ---
# openssl 3.1.4 at /usr/lib/x86_64-linux-gnu/libssl.so
# checksum: md5sum:5a2b3c...
echo "Verify: openssl version should be 3.1.4"

# --- container: myimage ---
docker build -t myimage:latest -f ./Dockerfile .
docker run -v $(pwd):/work myimage

# --- qemu: stm32 ---
module load qemu/8.2.0
# qemu 8.2.0 at /usr/bin/qemu-system-arm
# checksum: md5sum:a3f8b2c...

# --- toolchain: arm-gcc ---
module load gcc/13.2.0
# arm-none-eabi-gcc 13.2.0 at /usr/local/bin/arm-none-eabi-gcc
# checksum: md5sum:9c1d4e...
