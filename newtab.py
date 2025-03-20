import pyautogui
import time
import subprocess

def click_at(x, y, sleep_after=1):
    """Moves the cursor to (x, y) and clicks, then sleeps for a given time."""
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.click()
    time.sleep(sleep_after)

def type_text(text, sleep_after=1):
    """Types the given text, then sleeps."""
    pyautogui.write(text, interval=0.1)  # Types like a human
    time.sleep(sleep_after)

# Click on (517, 39)
click_at(517, 39, sleep_after=1)

# Click on (490, 84)
click_at(490, 84, sleep_after=1)

# Type "www.github.com"
type_text("www.github.com", sleep_after=1)

# Press Enter
pyautogui.press('enter')
time.sleep(4)  # Wait for the page to load

# Run "codespace.py" using subprocess
subprocess.run(["python3", "codespace.py"])

# Sleep 1 second after running the script
time.sleep(1)
