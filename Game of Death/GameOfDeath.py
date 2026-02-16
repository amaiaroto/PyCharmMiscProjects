import pygame as pg
import sys
import socket
import random

playerOnePos, playerTwoPos, playerThreePos = ({'x': 100, 'y': 30, 'speed': 1, 'size': 5},
                                              {'x': 125, 'y': 45, 'speed': 1, 'size': 5},
                                              {'x': 100, 'y': 55, 'speed': 1, 'size': 5})

pg.init()

screenSize = 1000
screen = pg.display.set_mode((screenSize, screenSize * 0.8))
font = pg.font.SysFont('Arial', 81)

pg.display.set_caption("Game of Death")
clock = pg.time.Clock()


def getColor():
    for i in ['red', 'blue', 'yellow', 'green', 'white']:
        yield i


class Player:
    def __init__(self, x: int, y: int, speed=1, size=5):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = next(getColor())


import threading

running = True


def receive(connection, address):
    global players
    try:
        while connection is not None and address is not None:
            players.append(Player(random.randint(10, 990), random.randint(10, 990)))
            chunk = connection.recv(500)

            if chunk is not None:
                data = chunk.decode('utf-16')

                print(address, data)

    except OSError as e:
        print(e)
        thread = threading.Thread(target=sendMessage, args=(connection, 'Too long of text_pos message (over 500 characters)'))

def sendMessage(address: tuple[str, int], message: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.sendto(message.encode('ascii'), address)


def accept():
    global running

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 3456))
    s.listen(5)

    while running:
        connection, address = s.accept()
        client = threading.Thread(target=receive, args=(connection, address))
        client.start()


t = threading.Thread(target=accept)
t.start()

players = []

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

            running = False
            sys.exit()

    screen.fill((0, 0, 0))

    for p in players:
        pg.draw.circle(screen, (255, 0, 0), (playerOnePos['x'], playerOnePos['y']), playerOnePos['size'])

    pg.display.flip()

    clock.tick(60)
