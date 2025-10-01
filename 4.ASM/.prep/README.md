***RISC-V***

# A **consistent RISC-V assembler/compiler toolchain** on both macOS (via Homebrew) and Windows (via Chocolatey). That’s doable. The cleanest option is to use the **GNU RISC-V toolchain (riscv-gnu-toolchain)** or its packaged distributions.

---

## 🖥 macOS (Homebrew)

On macOS you can install via a tap:

```bash
brew tap riscv-software-src/riscv
brew install riscv-gnu-toolchain
```

This gives you tools like:

* `riscv64-unknown-elf-as` → assembler
* `riscv64-unknown-elf-gcc` → C/C++ compiler
* `riscv64-unknown-elf-ld` → linker

You can now assemble RISC-V code, e.g.:

```bash
riscv64-unknown-elf-as prog.s -o prog.o
riscv64-unknown-elf-ld prog.o -o prog.elf
```

---

## 🪟 Windows (Chocolatey)

On Windows, Chocolatey has **prebuilt RISC-V GCC toolchains** you can install. For example:

```powershell
choco install riscv-gnu-toolchain
```

That installs the same `riscv64-unknown-elf-*` binaries as on macOS.

⚠️ Note: If you don’t see `riscv-gnu-toolchain` in the main Chocolatey repo, the alternative is **MSYS2 with riscv64-elf-gcc** (which also works well). You can install MSYS2 with choco:

```powershell
choco install msys2
```

Then inside MSYS2:

```bash
pacman -S riscv64-elf-gcc
```

---

## ✅ Result

With either Homebrew (macOS) or Chocolatey/MSYS2 (Windows), you’ll have the **same RISC-V assembler + GCC toolchain** (`riscv64-unknown-elf-*`) available. This ensures that **the same ASM code assembles and runs the same way** across both systems.

---

# **minimal assembly “Hello, World” for RISC-V** that you can test on both Mac and Windows with this toolchain?

Nice 😃 Let’s make a minimal **RISC-V “Hello, World”** in assembly that you can run with the exact same toolchain on both macOS and Windows.

We’ll use the **standard Linux system call interface** (via `ecall`) so you can test it in QEMU after assembling.

---

## 📄 `hello.s` (RISC-V Assembly)

```asm
    .section .data
msg:
    .asciz "Hello, World!\n"

    .section .text
    .globl _start

_start:
    # write(fd=1, buf=msg, count=14)
    li a7, 64          # syscall number for write (Linux RISC-V)
    li a0, 1           # fd = 1 (stdout)
    la a1, msg         # buffer address
    li a2, 14          # length of string
    ecall

    # exit(code=0)
    li a7, 93          # syscall number for exit
    li a0, 0           # exit code
    ecall
```

---

## 🔨 Build and Run

### 1. Assemble & Link

On both macOS and Windows (after installing the RISC-V toolchain):

```bash
riscv64-unknown-elf-as hello.s -o hello.o
riscv64-unknown-elf-ld hello.o -o hello.elf
```

Now you have `hello.elf`.

---

### 2. Run in QEMU (RISC-V emulator)

Install QEMU via brew/choco:

* macOS:

  ```bash
  brew install qemu
  ```
* Windows (Chocolatey):

  ```powershell
  choco install qemu
  ```

Run:

```bash
qemu-riscv64 ./hello.elf
```

You should see:

```
Hello, World!
```

