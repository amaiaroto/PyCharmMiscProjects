import keyboard
import time

key = input("key to spam: ")
toggle_key = "]"   # you can change this

spamming = False

print("Press ] to start/stop. Press ESC to quit.")

while True:
    if keyboard.is_pressed("esc"):
        break

    if keyboard.is_pressed(toggle_key):
        spamming = not spamming
        print("Spamming:", spamming)
        time.sleep(0.3)  # prevents double toggles

    if spamming:
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(0.01)
