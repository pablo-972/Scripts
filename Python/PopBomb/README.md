# PopBomb (Python Popup)

A simple Python script utilizing `tkinter`, `threading`, and `random` to spawn multiple graphical windows infinitely across the screen. 

## Description

The script creates an infinite loop inside multiple background threads, generating new `Tkinter` GUI windows (`PopBomb`) with randomized screen positions and a playful taunting message ("PRINGAO JAJAJAJAJAJAJA") in Comic Sans font.

Running this script will flood your desktop with windows very quickly, which can severely lag or freeze the operating system until the Python process is terminated.

## Requirements

The script uses built-in Python standard libraries (`tkinter`, `sys`, `threading`, `time`, `random`), so no external package installations (`pip`) are required. However, Tkinter must be available in your Python environment:
- **Ubuntu/Debian:** `sudo apt-get install python3-tk`
- **Fedora:** `sudo dnf install python3-tkinter`

## Usage

Run the script from your terminal:
```bash
python pop_bomb.py
```

Or run the binary in a Windows system:
```powershell
\PopBomb.exe
```
