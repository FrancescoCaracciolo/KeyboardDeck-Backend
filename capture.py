from pynput import keyboard
from time import sleep
from KeyboardDeck.network import NetworkManager
import json

controlOn = 0
network = NetworkManager('localhost', 42069)

def on_press(key):
    global controlOn
    try:
        print('{0}'.format(
            key.char))
        network.send_keypress("a")
        if controlOn % 2 == 1:
            pass
    except AttributeError:
        if (key == keyboard.Key.ctrl):
            controlOn += 1
        print('[{0}]'.format(
            key))

def on_release(key):
    global controlOn
    try:
        key.char
    except AttributeError:
        if (key == keyboard.Key.ctrl):
            controlOn += 1
listener = keyboard.Listener(on_press=on_press, on_release = on_release)
listener.start()

while 1:
    try:
        sleep(1)
    except KeyboardInterrupt:
        listener.stop()
        exit()