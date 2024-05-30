import pyautogui
import time

# Give the user time to open WhatsApp Desktop and select the chat window
time.sleep(5)

# The message to send
message = "meh"

# Number of times to send the message
count = 50

for _ in range(count):
    # Type the message
    pyautogui.typewrite(message)
    # Press enter to send the message
    pyautogui.press('enter')
    # Optional: Add a delay to avoid sending messages too quickly
    # time.sleep(0.2)
