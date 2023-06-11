from pynput.keyboard import Key, Controller
from pynput import mouse
import time

keybind_pressed = False

def on_click(x, y, button, pressed):
    global keybind_pressed
    if ( button == button.x2 ):
        keybind_pressed = True
    else:
        keybind_pressed = False
    if not pressed:
        # Stop listener
        return False

    
kb = Controller()

wordlist = open("wordlist.txt", "r")

for line in wordlist:
    while ( not keybind_pressed ):
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
    if ( keybind_pressed ):
        for char in line:
            kb.press(char)
            kb.release(char)
            time.sleep(0.01)
        kb.press(Key.enter)

        time.sleep(0.01)
        keybind_pressed = False