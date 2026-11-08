# desktop-activity-monitor
desktop-activity-monitor
# snifferENG 🕵️‍♂️

A lightweight, real-time activity tracking script for Windows built in Python. It automatically logs active window titles (browsers, games like Roblox, AI tools like Claude, and text editors) directly to a text file on your Desktop.

## ✨ Features
- **Real-time monitoring:** Tracks active window titles instantly using native Windows `ctypes`.
- **Smart filtering:** Ignores duplicate consecutive entries and system background task switches.
- **Zero dependencies:** Uses only Python standard libraries (`os`, `time`, `ctypes`, `datetime`).
- **Clean logging:** Saves timestamped logs to `activity_log.txt` on your Desktop.

## 🚀 How to Use
1. Make sure Python is installed on your Windows machine.
2. Download or clone the `snifferENG.py` script.
3. Run the script in PowerShell or Command Prompt:
   ```bash
   python snifferENG.py
