import pyautogui
import time
import subprocess
import sys


def detect_web_button(script_name):
    """Run an external script to detect the web button with up to 10 attempts."""
    attempt = 0
    max_attempts = 15

    while attempt < max_attempts:
        print(f"Detection attempt {attempt + 1}/{max_attempts}...")
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for the detection script to finish

        if process.returncode == 0:  # Success code indicates the button was found
            print("Web button detected successfully.")
            return True  # Exit the loop and return success
        else:
            print("Web button not detected. Retrying...")
            attempt += 1
            time.sleep(2)  # Wait before the next attempt

    print("Max detection attempts reached. Proceeding with fallback action...")
    return False  # Return failure after all attempts


def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(1)
    pyautogui.moveTo(1360, 603)  # Move mouse to (1360,603)
    time.sleep(0.5)  # Wait 0.5 seconds
    pyautogui.click(1360, 603)  # Click at (1360,603)
    time.sleep(1)  # Wait 1 second
    pyautogui.click(35, 595)  # Click at (35,595)
    time.sleep(1)  # Wait 1 second
    for _ in range(4):
        pyautogui.press("up")
        time.sleep(0.5)
    pyautogui.press("right")
    time.sleep(0.5)
    pyautogui.press("down")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write(
        "sudo mkdir -p /etc/apt/keyrings && curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | sudo tee /etc/apt/keyrings/google-chrome.asc > /dev/null && echo \"deb [signed-by=/etc/apt/keyrings/google-chrome.asc] http://dl.google.com/linux/chrome/deb stable main\" | sudo tee /etc/apt/sources.list.d/google-chrome.list > /dev/null && sudo apt update && sudo apt install -y git"
    )
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(20)
    pyautogui.write("git clone https://github.com/kongoro20/git2.git")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(8)
    pyautogui.write("cd git2")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write("source start.sh")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)


if __name__ == "__main__":
    # Total cycles of detection and fallback
    max_cycles = 5
    cycle = 0

    while cycle < max_cycles:
        print(f"Starting detection cycle {cycle + 1}/{max_cycles}...")

        # Step 1: Detect the web button
        button_detected = detect_web_button('desktop_button.py')

        if button_detected:
            # If the button is detected, exit the cycle and perform additional tasks
            print(f"Button detected during cycle {cycle + 1}. Proceeding to additional tasks.")
            perform_additional_tasks()
            break  # Exit the while loop if button is detected
        else:
            # Perform fallback click if the button is not detected after all attempts
            print(f"Button not detected during cycle {cycle + 1}. Performing fallback click.")
            pyautogui.click(96, 85)
            time.sleep(5)

        # Increment the cycle counter
        cycle += 1

    # If the script finishes all cycles without detecting the button
    if cycle == max_cycles:
        print(f"All {max_cycles} cycles completed without detecting the button.")
        sys.exit()
