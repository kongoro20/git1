import pyautogui
import time
import os

# Step 1: Sleep for 3 seconds before starting
time.sleep(3)

# Paths to the images of the verification buttons
verif_button_image = 'zone_button.png'
verif1_button_image = 'zone1_button.png'

# Maximum number of detection attempts
max_attempts = 1000

# Check if both image files exist
if not os.path.isfile(verif_button_image):
    print(f"Error: The image file '{verif_button_image}' does not exist.")
if not os.path.isfile(verif1_button_image):
    print(f"Error: The image file '{verif1_button_image}' does not exist.")

# Loop for a maximum number of attempts
for attempt in range(max_attempts):
    print(f"Attempt {attempt + 1} of {max_attempts}: Attempting to detect verification buttons...")

    # Sleep for 4 seconds before each detection attempt
    time.sleep(2)

    # Try to detect the first verification button: verif_button.png
    button_location = None
    try:
        print(f"Trying to detect: {verif_button_image}")
        button_location = pyautogui.locateOnScreen(verif_button_image, confidence=0.8)
    except Exception as e:
        print(f"Error while detecting '{verif_button_image}': {e}")

    # If the first button is detected, click it
    if button_location:
        print(f"'{verif_button_image}' detected at {button_location}, clicking...")
        time.sleep(1)  # Wait before clicking
        pyautogui.click(button_location)  # Click the detected button
        print(f"'{verif_button_image}' clicked!")
        break  # Exit the loop after clicking the button

    # If the first button is not found, attempt to detect the second button: verif1_button.png
    try:
        print(f"Trying to detect: {verif1_button_image}")
        button_location = pyautogui.locateOnScreen(verif1_button_image, confidence=0.8)
    except Exception as e:
        print(f"Error while detecting '{verif1_button_image}': {e}")

    # If the second button is detected, click it
    if button_location:
        print(f"'{verif1_button_image}' detected at {button_location}, clicking...")
        time.sleep(1)  # Wait before clicking
        pyautogui.click(button_location)  # Click the detected button
        print(f"'{verif1_button_image}' clicked!")
        break  # Exit the loop after clicking the button

    # If neither button is found, press the Down Arrow key and try again
    print(f"Neither '{verif_button_image}' nor '{verif1_button_image}' detected. Pressing Down Arrow key...")
    pyautogui.press('down')
    pyautogui.press('down')  # Press the Down Arrow key
    print("Down Arrow key pressed.")

else:
    print("Maximum detection attempts reached. Exiting...")
