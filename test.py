"""

Code Written by Claude Sonnet 4.5 for learning libraries.

Python Automation Tutorial - Learn the Libraries
A simple, modular script to learn keyboard, mouse, and pynput basics
Edit the variables and experiment with different values!
"""

import keyboard  # For keyboard control
import mouse    # For mouse clicks
import time      # For delays
from pynput.mouse import Controller  # For mouse position control

# ============================================
# CONFIGURATION - Edit these values to experiment!
# ============================================

# Which key to press? Try: 'w', 'a', 's', 'd', 'space', 'shift'
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

# ============================================
# LESSON 1: Keyboard Control
# ============================================

def lesson_keyboard():
    """Learn how to press and hold keys"""
    print("\n--- LESSON 1: Keyboard Control ---")
    
    # Press a key once (quick tap)
    print(f"Pressing '{KEY_TO_PRESS}' key once...")
    keyboard.press_and_release(KEY_TO_PRESS)
    time.sleep(1)  # Wait 1 second
    
    # Hold a key down for a duration
    print(f"Holding '{KEY_TO_PRESS}' key for {HOLD_DURATION} seconds...")
    keyboard.press(KEY_TO_PRESS)      # Press and hold
    time.sleep(HOLD_DURATION)         # Wait while holding
    keyboard.release(KEY_TO_PRESS)    # Release the key
    
    # Type multiple keys in sequence
    print("Typing 'hello' one key at a time...")
    keyboard.write('hello')  # Types each letter
    time.sleep(1)
    
    print("Keyboard lesson complete!\n")

# ============================================
# LESSON 2: Mouse Clicking
# ============================================

def lesson_mouse_clicks():
    """Learn how to click the mouse"""
    print("\n--- LESSON 2: Mouse Clicking ---")
    
    # Single click
    print(f"Clicking {MOUSE_BUTTON} mouse button once...")
    mouse.click(button=MOUSE_BUTTON)
    time.sleep(1)
    
    # Multiple clicks
    print(f"Clicking {CLICK_COUNT} times with {CLICK_DELAY}s delay...")
    for i in range(CLICK_COUNT):
        print(f"  Click {i + 1}/{CLICK_COUNT}")
        mouse.click(button=MOUSE_BUTTON)
        time.sleep(CLICK_DELAY)
    
    # Press and hold mouse button
    print(f"Holding {MOUSE_BUTTON} button for 2 seconds...")
    mouse.press(button=MOUSE_BUTTON)   # Press down
    time.sleep(2)                       # Hold for 2 seconds
    mouse.release(button=MOUSE_BUTTON) # Release
    
    print("Mouse clicking lesson complete!\n")

# ============================================
# LESSON 3: Mouse Position Control
# ============================================

def lesson_mouse_position():
    """Learn how to move and track the mouse cursor"""
    print("\n--- LESSON 3: Mouse Position ---")
    
    # Create a controller to manipulate mouse position
    mouse_ctrl = Controller()
    
    # Get current mouse position
    current_pos = mouse_ctrl.position
    print(f"Current mouse position: X={current_pos[0]}, Y={current_pos[1]}")
    time.sleep(1)
    
    # Move mouse to a specific position
    print(f"Moving mouse to X={MOUSE_X_POSITION}, Y={MOUSE_Y_POSITION}...")
    mouse_ctrl.position = (MOUSE_X_POSITION, MOUSE_Y_POSITION)
    time.sleep(1)
    
    # Move mouse relative to current position
    print("Moving mouse 100 pixels right and 50 pixels down...")
    mouse_ctrl.move(100, 50)  # (x_offset, y_offset)
    time.sleep(1)
    
    # Track mouse movement for 3 seconds
    print("Tracking mouse movement for 3 seconds (move your mouse!)...")
    start_time = time.time()
    last_pos = mouse_ctrl.position
    
    while time.time() - start_time < 3:
        current_pos = mouse_ctrl.position
        # Check if mouse moved
        if current_pos != last_pos:
            print(f"  Mouse moved to: X={current_pos[0]}, Y={current_pos[1]}")
            last_pos = current_pos
        time.sleep(0.1)  # Check every 0.1 seconds
    
    print("Mouse position lesson complete!\n")

# ============================================
# LESSON 4: Combining Actions
# ============================================

def lesson_combination():
    """Learn how to combine keyboard and mouse actions"""
    print("\n--- LESSON 4: Combining Actions ---")
    
    print("Simulating a simple pattern:")
    print("  1. Press 'w' key")
    print("  2. Click mouse 3 times")
    print("  3. Release 'w' key")
    
    time.sleep(2)  # Give you time to read
    
    # Press and hold 'w'
    keyboard.press('w')
    print("Holding 'w' key...")
    
    # Click 3 times while holding 'w'
    for i in range(3):
        print(f"  Click {i + 1}")
        mouse.click()
        time.sleep(0.5)
    
    # Release 'w'
    keyboard.release('w')
    print("Released 'w' key")
    
    print("Combination lesson complete!\n")

# ============================================
# LESSON 5: Hotkeys (Keyboard Shortcuts)
# ============================================

def lesson_hotkeys():
    """Learn how to create custom keyboard shortcuts"""
    print("\n--- LESSON 5: Hotkeys ---")
    print("Setting up hotkeys...")
    print("  Press 'q' to print a message")
    print("  Press 'ESC' to exit this lesson")
    
    # Flag to track if we should exit
    exit_lesson = False
    
    # Function that runs when 'q' is pressed
    def on_q_pressed():
        print("You pressed 'q'! Hello from the hotkey!")
    
    # Function that runs when 'ESC' is pressed
    def on_esc_pressed():
        nonlocal exit_lesson  # Access the outer variable
        print("ESC pressed - exiting lesson...")
        exit_lesson = True
    
    # Register the hotkeys
    keyboard.add_hotkey('q', on_q_pressed)
    keyboard.add_hotkey('esc', on_esc_pressed)
    
    # Wait for ESC to be pressed
    while not exit_lesson:
        time.sleep(0.1)
    
    # Clean up hotkeys
    keyboard.remove_hotkey('q')
    keyboard.remove_hotkey('esc')
    
    print("Hotkey lesson complete!\n")

# ============================================
# MAIN MENU
# ============================================

def main():
    print("=" * 50)
    print("Python Automation Tutorial")
    print("=" * 50)
    print("\nChoose a lesson to run:")
    print("  1 - Keyboard Control")
    print("  2 - Mouse Clicking")
    print("  3 - Mouse Position")
    print("  4 - Combining Actions")
    print("  5 - Hotkeys")
    print("  6 - Run All Lessons")
    print("  0 - Exit")
    print("=" * 50)
    
    choice = input("\nEnter lesson number: ")
    
    if choice == '1':
        lesson_keyboard()
    elif choice == '2':
        lesson_mouse_clicks()
    elif choice == '3':
        lesson_mouse_position()
    elif choice == '4':
        lesson_combination()
    elif choice == '5':
        lesson_hotkeys()
    elif choice == '6':
        lesson_keyboard()
        lesson_mouse_clicks()
        lesson_mouse_position()
        lesson_combination()
        lesson_hotkeys()
    elif choice == '0':
        print("Goodbye!")
        return
    else:
        print("Invalid choice!")
    
    # Ask if they want to continue
    again = input("\nRun another lesson? (y/n): ")
    if again.lower() == 'y':
        main()

# Run the program
if __name__ == "__main__":
    main()