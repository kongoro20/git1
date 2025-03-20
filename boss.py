import pyautogui
import time
import subprocess

def detect_button_via_script(script_name):
    """Run an external script to detect a button and keep trying until it succeeds."""
    while True:  # Loop until the button is found
        # Start the external script
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for it to finish

        if process.returncode == 0:  # Check if the button was found
            print(f"Button in {script_name} detected and clicked!")
            return
        else:
            print(f"Button in {script_name} not detected, retrying...")
            time.sleep(2)  # Wait 2 seconds before retrying detection

if __name__ == "__main__":
    # Step 1: Detect the main button via main.py script
    detect_button_via_script('main.py')

    print("Main button detected and clicked. Waiting for page to load...")
    time.sleep(10)  # Wait for the page to load

    # Step 2: Press Tab 19 times and type the Docker command
    for _ in range(19):
        pyautogui.press("tab")
    pyautogui.write("docker run -p 6500:80 dorowu/ubuntu-desktop-lxde-vnc")
    time.sleep(5)
    pyautogui.press("enter")
    print("Docker command typed and executed.")
    time.sleep(4)
    # Step 3: Run error.py before detecting the browser button
    print("Running error.py before Step 3...")
    subprocess.run(['python3', 'error.py'])  # Run error.py
    time.sleep(25)  # Wait after running error.py

    # Detect the browser button via browser.py script
    detect_button_via_script('browser.py')
    time.sleep(5)

    # Step 4: Detect the desktop button via desktop.py script
    subprocess.run(['python3', 'desktop.py'])

    # Step 5: Perform additional desktop actions
    print("Performing desktop actions...")
    
    
   
