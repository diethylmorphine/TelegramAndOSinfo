# OPTIONAL INFORMATION

This guide explains how to package a Python application into an executable using **PyInstaller** and how to protect your source code using **PyArmor**.

---

## Installation

```bash
pip install pyinstaller pyarmor
```

---

# PyInstaller — Building Executable Files

PyInstaller packages your script and its dependencies into a standalone executable.

## Basic usage

Build a standard executable:

```bash
pyinstaller script.py
```

The result will appear in `dist/script/`.

## Useful options

### One-file build

```bash
pyinstaller --onefile script.py
```

### Disable console window (for GUI applications)

```bash
pyinstaller --onefile --windowed script.py
```

### Add an icon

```bash
pyinstaller --onefile --icon=app.ico script.py
```

### Include additional files

```bash
pyinstaller --onefile --add-data "config.json;." script.py
```

---

# PyArmor — Protecting Python Code

PyArmor encrypts Python files to make reverse engineering more difficult.

## Initialize a project

```bash
pyarmor init --src=src --entry=main.py project
```

## Obfuscate and build

```bash
pyarmor build project
```

Protected files will appear in the `dist/` directory.

## Obfuscate a single script

```bash
pyarmor obfuscate script.py
```

The obfuscated file will be located in `dist/`.

---

# Using PyInstaller and PyArmor Together

1. Obfuscate your script:

   ```bash
   pyarmor obfuscate --output obf script.py
   ```
2. Build an executable from the obfuscated version:

   ```bash
   pyinstaller --onefile obf/script.py
   ```

---

# Additional Tips

* Use `--onefile` only when necessary; it increases startup time.
* Do not obfuscate third-party libraries. Protect only your own code.
* Test the final executable in a clean environment or virtual machine.
