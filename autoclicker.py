import time
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener
import threading

toggle_key = KeyCode(char = 'k')

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)

def toggle_event(key):
    if key == toggle_key:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target = clicker)
click_thread.start()

with Listener(on_press = toggle_event) as listener:
    listener.join()