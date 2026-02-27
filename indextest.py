

import pyautogui
import keyboard
import time

print("Move your mouse to the target location.")
print("Press 's' to save the position.")
print("Press 'c' to click the saved position.")
print("Press 'q' to quit.")

saved_position = None

time.sleep(2)

while True:
    x, y = pyautogui.position()
    print(f"Current Position -> X: {x}, Y: {y}", end="\r")

    # Save position
    if keyboard.is_pressed('s'):
        saved_position = (x, y)
        print(f"\nPosition Saved at X: {x}, Y: {y}")
        time.sleep(1)

    # Click saved position
    if keyboard.is_pressed('c'):
        if saved_position:
            print("\nClicking saved position...")
            pyautogui.click(saved_position)
            time.sleep(1)
        else:
            print("\nNo position saved yet!")

    # Quit program
    if keyboard.is_pressed('q'):
        print("\nExiting program...")
        break

