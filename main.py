from pynput import keyboard
from pynput.keyboard import Key, Controller
import pynput
from pynput import mouse
import time

keybind_pressed = False

# def on_press(key):
#     # try:
#     #     print('alphanumeric key {0} pressed'.format(key.char))
#     # except AttributeError:
#     #     print('special key {0} pressed'.format(key))
#     if ( key == keyboard.Key.shift_r ):
#         global keybind_pressed
#         keybind_pressed = True
# 
#     
# 
# def on_release(key):
#     #print('{0} released'.format(key))
#     global keybind_pressed
#     keybind_pressed = False
# 
# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()

def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed:
        # Stop listener
        return False


# # ...or, in a non-blocking fashion:
# listener = mouse.Listener(on_click=on_click)
# listener.start()

    
type = Controller()

wordlist = open("wordlist.txt", "r")

for line in wordlist:
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    for char in line:
        type.press(char)
        type.release(char)
        time.sleep(0.01)
        print(char)
    type.press(Key.enter)
    time.sleep(0.2)