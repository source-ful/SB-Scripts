"""

This script functions as a precursour for the farming.py script, due to my lack of knowledge of the libraries used.
As a result, this simple script will function to teach my the libraries aswell as principles of automation.

This script will not be used in the final product, but will be used to teach me the libraries and principles of automation.
Note: While this script will not be used in the final product, it will be included in the repository for reference & documentation.

"""
# Importing libraries

import keyboard
import mouse
import time
import threading    
from pynput.mouse import Controller, Button


# Configuration:

KEY_TO_PRESS = 'w'

# How long to hold the key down (in seconds)
HOLD_DURATION = 2

# How many times to click the mouse
CLICK_COUNT = 5

# Delay between clicks (in seconds)
CLICK_DELAY = 0.5

# Mouse button to use: 'left', 'right', or 'middle'
MOUSE_BUTTON = 'left'

# Where to move the mouse (x, y coordinates on screen)
MOUSE_X_POSITION = 500
MOUSE_Y_POSITION = 500

# Functions:

# Main Function:
def main():
    print("Starting script...")
    time.sleep(1)
    print("\nScript started!")
    time.sleep(1)
    print("\nScript stopping...")
    time.sleep(1)
    print("\nScript finished!")

if __name__ == "__main__":
    main()