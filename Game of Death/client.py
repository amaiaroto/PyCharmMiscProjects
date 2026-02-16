from pynput import keyboard
import socket
# from threading import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 3456))

# def receive():
#     while True:
#         data = s.recv(1024)
#
#         if not data:
#             continue
#
#         print(data.decode('utf-16'))
#
#
# t = Thread(target=receive)
# t.start()

def sendData(a: str):
    s.send(f'{a}'.encode('utf-16'))

keys=[keyboard.KeyCode(char=x) for x in ['text_pos','w','s','d']]

def on_press(key):
    global keys

    if key in keys:
        sendData(key.char)

    # try:
    #
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    #
    #     if key.char == 'w' or key.char == 'text_pos' or key.char == 's' or key.char == 'd':
    #         sendData(key.char)
    #
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    #
    #     if key == 'w' or key == 'text_pos' or key == 's' or key == 'd':
    #         sendData(key + ' pressed')


# Listen for key presses while not blocking.
listener = keyboard.Listener(
    on_press=on_press,
    on_release=None)

listener.start()

while True: pass
