
# Import the keyboard library to simulate keypresses
import keyboard
# Import the mouse library to simulate mouse clicks
import mouse
# Import time library for delays and sleep functions
import time
# Import threading to run multiple functions at the same time
import threading
# Import pynput's mouse Controller to get and set mouse position
from pynput.mouse import Controller, Button

# Reference Variables:
running = False
exit_flag = False
movement_key = 'a'
mouse_button = 'left'

# Print Status Statements:
def print_func():
    print("\n--------------------------------\n")
    print("Minecraft Farming Macro ~ Ready!")
    print("Controls:")
    print("F1: Start/Stop the farming macro.")
    print("ESC: Exit the script.")
    print("Press F1 to begin the script.")
    print("\n--------------------------------\n")

# Keyboard Functions:
def key_func():
    global running, exit_flag, movement_key

    if keyboard.is_pressed('f1'):
        running = not running
        if running:
            print("Farming script started!")