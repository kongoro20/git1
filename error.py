import pyautogui
import time
import os

# Path to the image of the main button
main_button_image = 'main_button.png'
time.sleep(2)
# Check if the image file exists
if not os.path.isfile(main_button_image):
    print(f"Error: The image file '{main_button_image}' does not exist.")
else:
    while True:
        # Attempt to locate the main button
        button_location = None
        try:
            button_location = pyautogui.locateOnScreen(main_button_image, confidence=0.8)
        except Exception as e:
            print(f"Error while detecting the main button: {e}")

        # Check if the button is found
        if button_location:
            print("Main button detected. Performing actions...")
            time.sleep(4)
            pyautogui.press('up')  # Press the up arrow key
            time.sleep(1)
            pyautogui.press('enter')  # Press Enter
            time.sleep(5)
        else:
            # Exit if the button is no longer detected
            print("Main button no longer detected. Exiting...")
            break
