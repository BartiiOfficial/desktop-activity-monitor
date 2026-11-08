import os
import time
import ctypes
from datetime import datetime

# Path to the log file on the Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "activity_log.txt")
last_activity = ""

def get_active_window_title():
    """Fetches the title of the currently active foreground window on Windows."""
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
    return buff.value

print("=== snifferENG (Desktop Activity Monitor) ===")
print(f"Logging activity to: {desktop_path}")
print("Monitoring open windows, games (e.g., Roblox), and apps (e.g., Claude)...")
print("Press CTRL + C in the terminal to stop.\n")

while True:
    try:
        current_window = get_active_window_title()
        
        # Log only if the active window title changes and is not empty
        if current_window and current_window != last_activity:
            # Filter out empty or system background tasks
            if len(current_window) > 2 and "Task View" not in current_window and "Switching" not in current_window:
                last_activity = current_window
                timestamp = datetime.now().strftime("%H:%M:%S")
                
                log_entry = f"[{timestamp}] ---> {current_window}"
                print(log_entry)
                
                # Append the entry directly to the text file
                with open(desktop_path, "a", encoding="utf-8") as file:
                    file.write(log_entry + "\n")
    except Exception:
        pass

    # Check for active window changes every 0.5 seconds
    time.sleep(0.5)