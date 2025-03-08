import keyboard
import time

SPECIAL_CHARACTER = "​"  # Change this to any character you want

def type_character():
    time.sleep(0.1)  # Small delay to prevent issues
    keyboard.write(SPECIAL_CHARACTER)

keyboard.add_hotkey("F2", type_character)

print("Script running... Press CTRL + ALT to type the special character.")
keyboard.wait()  # Keeps the script running
