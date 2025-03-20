import pyautogui
import subprocess
import time

# Time to wait in each tab (seconds)
WAIT_TIME = 4

def get_all_firefox_windows():
    """Retrieve all Firefox windows, including minimized ones."""
    result = subprocess.run(['xdotool', 'search', '--name', 'Mozilla Firefox'], stdout=subprocess.PIPE)
    window_ids = result.stdout.decode().splitlines()
    return window_ids

def is_window_minimized(window_id):
    """Check if a window is minimized using xprop."""
    result = subprocess.run(['xprop', '-id', window_id], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if b'_NET_WM_STATE_HIDDEN' in result.stdout:
        return True
    return False

def activate_window(window_id):
    """Focus on a specific window and bring it to the foreground."""
    subprocess.run(['xdotool', 'windowactivate', '--sync', window_id])

def minimize_window(window_id):
    """Minimize a specific window."""
    subprocess.run(['xdotool', 'windowminimize', window_id])

def navigate_four_tabs():
    """Navigate through four tabs in each Firefox window with additional actions."""
    # Click at (143, 42) after focusing on the window
    pyautogui.click(143, 42)
    time.sleep(1)

    # First tab: Click (693, 580) and wait
    pyautogui.click(693, 580)
    time.sleep(WAIT_TIME)

    # Second tab: Refresh, then wait
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)
    pyautogui.click(95, 82)  # Refresh the page
    time.sleep(WAIT_TIME)

    # Third tab: Click (693, 580) and wait
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)
    pyautogui.click(693, 580)
    time.sleep(WAIT_TIME)

    # Fourth tab: Refresh, then wait
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)   # Refresh the page
    pyautogui.click(95, 82) 
    time.sleep(WAIT_TIME)

if __name__ == "__main__":
    # Step 1: Get list of all Firefox windows
    firefox_windows = get_all_firefox_windows()

    # Step 2: Loop through each Firefox window, focusing only on minimized ones
    for window_id in firefox_windows:
        if is_window_minimized(window_id):
            print(f"Focusing on minimized Firefox window ID: {window_id}")

            # Activate (focus on) the minimized window
            activate_window(window_id)
            time.sleep(1)  # Allow time for the window to activate

            # Step 3: Navigate through four tabs, performing actions on each tab
            navigate_four_tabs()

            # Step 4: Minimize the window after finishing with its tabs
            minimize_window(window_id)
            print(f"Minimized Firefox window ID: {window_id}")
