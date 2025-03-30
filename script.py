import pyautogui
import random
import time
import subprocess
import string
import sys  # Import sys to exit fully

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
    return times  # Return the number of times pressed

def generate_random_name(min_length, max_length):
    """Generates a random name where each consonant is followed by a vowel."""
    length = random.randint(min_length, max_length)
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    name = "".join(random.choice(consonants) + random.choice(vowels) for _ in range(length // 2))
    return name[:length]  # Ensure the length matches exactly

def type_like_human(text):
    """Types text with a random human-like delay between keystrokes."""
    for char in text:
        pyautogui.write(char, interval=random.uniform(0.1, 0.3))
    print(f"Typed: {text}")

# Function to click at specified coordinates
def click_at(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

time.sleep(4)

# Function to generate a random word of given length
def random_word(min_len, max_len):
    length = random.randint(min_len, max_len)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# New Step: Detect the tab button using 'tab_button.png'
try:
    tab_button_location = pyautogui.locateCenterOnScreen('tab_button.png', confidence=0.8)
    if tab_button_location is not None:
        print("Tab button detected, clicking at (1342, 125)...")
        click_at(1342, 125)
        time.sleep(2)
    else:
        print("Tab button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting tab button: {e}")
    print("Proceeding to Step 1...")

time.sleep(2)

try:
    tab_button_location = pyautogui.locateCenterOnScreen('outlook_button.png', confidence=0.8)
    if tab_button_location is not None:
        print("Tab button detected, clicking at (1342, 125)...")
        time.sleep(0.7)
        click_at(253, 41)
        time.sleep(2)
    else:
        print("outlook button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting outlook button: {e}")
    print("Proceeding to Step 1...")

# Step 1: Previous tasks
time.sleep(2)
click_at(322, 82)
pyautogui.write("www.github.com")
time.sleep(0.7)
pyautogui.press("enter")
time.sleep(random.uniform(6, 8))

try:
    copilot_button_location = pyautogui.locateCenterOnScreen('copilot_button.png', confidence=0.8)
    if tab_button_location is not None:
        print("Copilot button detected, clicking at (1310, 172)...")
        click_at(1310, 172)
        time.sleep(1.5)
    else:
        print("Copilot button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting copilot button: {e}")
    print("Proceeding to Step 1...")

time.sleep(2)

# Here you will incorporate sign detection button
try:
    sign_button_location = pyautogui.locateCenterOnScreen('sign_button.png', confidence=0.8)
    if sign_button_location is not None:
        print("Sign button detected, performing additional clicks...")
        time.sleep(0.5)
        pyautogui.click(sign_button_location)
        time.sleep(7)
    else:
        print("Sign button not detected, proceeding to Step 1-a...")
except Exception as e:
    print(f"Error detecting sign button: {e}")
    print("Proceeding to Step 1-a...")

time.sleep(1)

try:
    cookie_button_location = pyautogui.locateCenterOnScreen('acceptcookie_button.png', confidence=0.8)
    if cookie_button_location is not None:
        print("cookie button detected, performing additional clicks...")
        time.sleep(0.5)
        pyautogui.click(cookie_button_location)
        time.sleep(1.5)
        random_click(569, 494, 789, 506)
        time.sleep(7)
    else:
        print("cookie button not detected, proceeding to Step 1-a...")
        time.sleep(0.5)
        random_click(569, 494, 789, 506)
        time.sleep(7)
except Exception as e:
    print(f"Error detecting cookie button: {e}")
    print("Proceeding to Step 1-a...")
    time.sleep(0.5)
    random_click(569, 494, 789, 506)
    time.sleep(7)

time.sleep(2)

try:
    select_button_location = pyautogui.locateCenterOnScreen('select_button.png', confidence=0.8)
    if select_button_location is not None:
        print("Select button detected, performing additional clicks...")
        time.sleep(0.5)
        pyautogui.click(select_button_location)
        time.sleep(7)
    else:
        print("Select button not detected, proceeding to Step 1-a...")
except Exception as e:
    print(f"Error detecting select button: {e}")
    print("Proceeding to Step 1-a...")

# Start execution
random_sleep(2, 2)

def detect_web_button(script_name):
    """Run an external script to detect the web button with up to 10 attempts."""
    attempt = 0
    max_attempts = 5

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
    button_detected = detect_web_button('ban.py')

    if button_detected:
        # If the button is detected, exit the cycle and perform additional tasks
        print(f"Button detected during cycle {cycle + 1}. Proceeding to additional tasks.")
        time.sleep(0.7)
        pyautogui.click(1358, 11)
        time.sleep(2)
        subprocess.run(["bash", "gofile.sh"])
        time.sleep(1.5)
        subprocess.run(['python3', 'script.py'])
        
        # **Fully exit the script after the required actions**
        sys.exit(0)  # Ensures the script stops execution

    else:
        # Perform fallback click if the button is not detected after all attempts
        print(f"Button not detected during cycle {cycle + 1}. Performing fallback click.")
        subprocess.run(['python3', 'complete.py'])

    # Increment the cycle counter
    cycle += 1
