#LetMePlayCoockieClicker
import ctypes
import threading
from pynput import keyboard

auto_clicking = False
running = True

MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004


def click_mouse():
    while running:
        if auto_clicking:
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def on_key_press(key):
    global auto_clicking
    global running
    if key == keyboard.Key.delete:
        auto_clicking = not auto_clicking
    if key == keyboard.Key.esc:
        running = False
        return False


auto_click_thread = threading.Thread(target=click_mouse)
auto_click_thread.start()


with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()