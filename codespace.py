import pyautogui
import random
import time
import subprocess

def random_click(x1, y1, x2, y2):
    """Performs a random click within the given rectangular area."""
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 0.7))
    pyautogui.click()
    print(f"Clicked at ({x}, {y})")

def random_sleep(min_sec, max_sec):
    """Sleeps for a random time between min_sec and max_sec seconds."""
    sleep_time = random.uniform(min_sec, max_sec)
    time.sleep(sleep_time)
    print(f"Slept for {sleep_time:.2f} seconds")

def press_key_random_times(key, min_times, max_times, min_sleep, max_sleep):
    """Presses a key randomly between min_times and max_times, with random sleep in between."""
    times = random.randint(min_times, max_times)
    for _ in range(times):
        pyautogui.press(key)
        random_sleep(min_sleep, max_sleep)

# Start execution
random_click(1138, 178, 1173, 188)
random_sleep(1, 1.5)

random_click(1152, 302, 1289, 313)
random_sleep(3, 3)

random_click(903, 344, 1032, 355)
random_sleep(1, 1)

# Press down arrow randomly (1-7 times) with 0.5s delay
press_key_random_times('down', 1, 7, 0.5, 0.5)

# Press Enter
pyautogui.press('enter')
random_sleep(0.8, 0.8)

random_click(1102, 277, 1324, 551)
random_sleep(0.7, 0.7)

# Press down arrow 6-8 times with a random 0.5-0.7s delay
press_key_random_times('down', 6, 8, 0.5, 0.7)

random_sleep(1, 1)

random_click(913, 448, 1036, 460)
time.sleep(4)

def detect_web_button(script_name):
    """Run an external script to detect the web button with up to 10 attempts."""
    attempt = 0
    max_attempts = 10

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

max_cycles = 1
cycle = 0

while cycle < max_cycles:
    print(f"Starting detection cycle {cycle + 1}/{max_cycles}...")

    # Step 1: Detect the web button
    button_detected = detect_web_button('ban1.py')

    if button_detected:
        # If the button is detected, exit the cycle and perform additional tasks
        print(f"Button detected during cycle {cycle + 1}. Proceeding to additional tasks.")
        time.sleep(0.7)
        pyautogui.click(1358, 11)
        time.sleep(2)
        subprocess.run(["bash", "gofile.sh"])
        time.sleep(1.5)
        subprocess.run(['python3', 'script.py'])
        time.sleep(1)
        subprocess.run(['python3', 'codespace.py'])

        # **Fully exit the script after the required actions**
        sys.exit(0)  # Ensures the script stops execution

    else:
        # Perform fallback click if the button is not detected after all attempts
        print(f"Button not detected during cycle {cycle + 1}. Performing fallback click.")
        time.sleep(20)
        pyautogui.click(420, 315)
        time.sleep(2)

    # Increment the cycle counter
    cycle += 1

