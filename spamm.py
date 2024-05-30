import pyautogui
import time

# Function to delay execution for a given number of milliseconds
def delay(ms):
    time.sleep(ms / 1000)

# Function to type and send a message multiple times
def send_messages(message, count):
    for _ in range(count):
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        delay(1000)  # 1 second delay between messages

# Main function to run the script
def main():
    message = "Hello, this is a test message!"  # The message to send
    count = 10  # Number of times to send the message

    print('You have 5 seconds to focus on the WhatsApp Desktop window...')
    delay(5000)  # 5 seconds to switch to WhatsApp Desktop
    send_messages(message, count)
    print('Messages sent!')

if __name__ == "__main__":
    main()
