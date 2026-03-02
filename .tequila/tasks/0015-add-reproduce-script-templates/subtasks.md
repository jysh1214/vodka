# Subtasks of *Add Reproduce Script Templates*

## Create templates

- [x] Create `assets/templates/reproduce.sh` based on the example YAML: pyvenv/.venv section, dep/openssl section, container/myimage section, qemu/stm32 section, toolchain/arm-gcc section
- [x] Create `assets/templates/experiment-steps.sh` based on the example YAML: exec/firmware section with cd, build, run (list), expect (list), and a QEMU delegation example
- [x] Create `assets/templates/run_qemu.py` showing the pexpect pattern: spawn, sendline, expect, close

## Update references

- [x] Add template references to `references/reproduce.md` under each output script section
