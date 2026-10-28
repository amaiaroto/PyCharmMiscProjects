from asciimatics.screen import Screen
from random import randint
from time import sleep


w, h = 50, 25
print(w*h)


def demo(screen):
    while True:

        screen.refresh()


Screen.wrapper(demo)
