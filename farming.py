
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
mouse_held = False

# Print Status Statements:
def print_func(): # Starting print statement to make everything look pretty.
    print("\n--------------------------------\n")
    print("Minecraft Farming Macro ~ Ready!")
    print("Controls:")
    print("F1: Start/Stop the farming macro.")
    print("ESC: Exit the script.")
    print("Press F1 to begin the script.")
    print("\n--------------------------------\n")

# Keyboard Functions:
def key_func(): # Keyboard function for movement.
    global running, exit_flag, movement_key

    if keyboard.is_pressed('f1'):
        running = not running
        if running:
            print("Farming script started!")
        else:
            print("\nFarming script stopped!")
        time.sleep(0.5) # To prevent multiple quick toggles.
    if keyboard.is_pressed('esc'):
        exit_flag = True
        print("\nScript exiting...")
        time.sleep(0.5)

def move_character():
    keyboard.press(movement_key)
    print(f"Moving {movement_key.upper()} sideways!\n")

def release_move_character():
    keyboard.release(movement_key)
    print("Stopping movement...\n")

def hold_mouse_button():
    mouse.press(mouse_button)
    print("\nMouse clicking begining!")

def release_mouse_button():
    mouse.release(mouse_button)
    print("\nMouse movement ending...")

# Main Function

# Main program
def main():
    global mouse_held
    
    print_func()  # Show welcome message
    
    while not exit_flag:  # Keep running until user presses ESC
        key_func()        # Check for key presses
        
        if running:       # If farming is active
            # Start holding mouse button if not already held
            if not mouse_held:
                hold_mouse_button()
                mouse_held = True
            
            # Move character sideways
            move_character()
            
        else:             # If farming is stopped
            # Release mouse button if still held
            if mouse_held:
                release_mouse_button()
                mouse_held = False
            
            time.sleep(0.1)  # Small delay when not farming
    
    # Clean up when exiting
    if mouse_held:
        release_mouse_button()
    
    print("Script ended!")

# Start the program
if __name__ == "__main__":
    main()