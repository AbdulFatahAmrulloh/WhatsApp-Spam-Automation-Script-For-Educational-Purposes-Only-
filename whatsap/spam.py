import pyautogui as p
import pyperclip  # Clipboard library
import time

time.sleep(4)
for i in range(1000):
    pyperclip.copy("nght sayang😘🩷")  # Copies the text to clipboard
    p.hotkey("ctrl", "v")  # Pastes the text
    p.press("enter")
