import pyautogui
import subprocess
import time

# Time to wait in each tab (seconds)
WAIT_TIME = 10

def get_latest_firefox_window():
    """Retrieve the most recent Firefox window ID."""
    result = subprocess.run(['xdotool', 'search', '--name', 'Mozilla Firefox'], stdout=subprocess.PIPE)
    window_ids = result.stdout.decode().splitlines()
    if window_ids:
        return window_ids[-1]  # Return the most recently opened Firefox window
    return None

def activate_window(window_id):
    """Focus on a specific window and bring it to the foreground."""
    if window_id:
        print(f"Activating Firefox window ID: {window_id}")
        subprocess.run(['xdotool', 'windowactivate', '--sync', window_id])
        time.sleep(2)  # Give time for activation
    else:
        print("No Firefox window detected!")

def close_all_firefox_windows():
    """Close all Firefox windows instead of minimizing them."""
    subprocess.run(["bash", "-c", """
    while wmctrl -l | grep -i "Mozilla Firefox" >/dev/null; do
        wmctrl -c "Mozilla Firefox"
        sleep 0.5
    done
    """])

def navigate_four_tabs():
    """Navigate through four tabs in each Firefox window with additional actions."""
    print("Starting tab navigation...")

    time.sleep(3)  # Wait before starting interactions
    pyautogui.click(143, 42)
    time.sleep(25)
    # First tab: Click (693, 580) and wait
    pyautogui.click(693, 580)
    time.sleep(WAIT_TIME)

    # Second tab: Refresh, then wait
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(2)
    pyautogui.click(95, 82)  # Refresh the page
    time.sleep(15)

    # Third tab: Click (693, 580) and wait
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(25)
    pyautogui.click(693, 580)
    time.sleep(WAIT_TIME)

    # Fourth tab: Refresh, then wait
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(2)
    pyautogui.click(95, 82)  # Refresh the page
    time.sleep(15)

if __name__ == "__main__":
    print("Detecting latest Firefox window...")
    firefox_window = get_latest_firefox_window()

    if firefox_window:
        activate_window(firefox_window)
        navigate_four_tabs()
        print("Navigation complete. Closing Firefox in 2 seconds...")
        time.sleep(2)
        close_all_firefox_windows()
    else:
        print("No active Firefox window found!")
