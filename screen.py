import pyautogui
import time
import pyperclip
import re
import subprocess



time.sleep(2)
pyautogui.press('f12')
time.sleep(4)
pyautogui.click(1302, 380)
time.sleep(2)
pyautogui.click(450, 193)
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.write("1366")
time.sleep(1)
pyautogui.click(506, 197)
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.write("641")
time.sleep(1)
pyautogui.click(1180, 193)
time.sleep(1)
pyautogui.click(1354, 379)
time.sleep(2)
pyautogui.click(442,81)
time.sleep(1)
# Press 'Ctrl + V' to paste the clipboard content
pyautogui.hotkey('ctrl', 'v')

# Sleep for 1 second
time.sleep(1)

# Press 'Enter' to submit
pyautogui.press('enter')

# Wait for 5 seconds for the page to finish loading
time.sleep(5)
