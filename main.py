import pyautogui
import time

def wait_for_main_button(image_path='main_button.png', confidence_level=0.8):
    """Continuously wait for the main button to appear until found."""
    print(f"Waiting for {image_path} to appear...")

    while True:  # Infinite loop until button is found
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence_level, grayscale=True)
        if button_location:
            print(f"{image_path} found at {button_location}. Clicking...")
            pyautogui.click(button_location)
            return 0  # Return success code

        time.sleep(0.5)  # Sleep briefly before checking again

if __name__ == "__main__":
    result = wait_for_main_button()
    if result == 0:
        exit(0)  # Success
    else:
        exit(1)  # Fail
