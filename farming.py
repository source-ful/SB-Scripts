"""
Farming script for Minecraft's Hypixel Skyblock.
This script is designed to farm resources for the player.
It is a work in progress and will be updated as the game is updated.

Features:
- The script should make the player move nonstop in one direction until something blocks the movement (like running into a wall or the edge of the area).

During the entire process, it should constantly hold down the left mouse button, so harvesting never stops.

If the normal farming motion gets disrupted — for example:

Macro-checked by an anti-macro protocol, whether it be an admin or just the server itself.

Or anything interrupts the usual pattern —
the script should be able to detect that interruption and react accordingly, instead of continuing blindly.
"""


"""
Minecraft Farming Script with Interruption Detection
Press F1 to start/stop farming
Press ESC to exit the script
"""

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