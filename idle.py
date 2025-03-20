import pyautogui
import time
import subprocess

def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.write("240")
    time.sleep(1)
    subprocess.run(["python3", "suitidle.py"])
    time.sleep(2.5)
    pyautogui.click(97, 84)
    time.sleep(2.5) 
    print("All tasks completed.")

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    subprocess.run(["python3", "detect.py"])

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
