import pygame as pg
import sys

pg.init()

screen = pg.display.set_mode((1000, 800))
squarePos = [screen.get_width() // 4, screen.get_height() // 2, 100, 100]
circlePos = [screen.get_width() // 2, screen.get_height() // 2]
speed = 1


def moveSquare():
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        squarePos[0] -= speed

    if keys[pg.K_RIGHT]:
        squarePos[0] += speed

    if keys[pg.K_UP]:
        squarePos[1] -= speed

    if keys[pg.K_DOWN]:
        squarePos[1] += speed


def moveCircle():
    key = pg.key.get_pressed()

    if key[pg.K_a]:
        circlePos[0] -= speed

    if key[pg.K_d]:
        circlePos[0] += speed

    if key[pg.K_w]:
        circlePos[1] -= speed

    if key[pg.K_s]:
        circlePos[1] += speed


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        pg.quit()
        sys.exit()

    screen.fill((255, 255, 255))

    pg.draw.circle(screen, (0, 0, 255), circlePos, 50)
    moveCircle()

    pg.draw.rect(screen, (255, 0, 0), squarePos)
    moveSquare()

    pg.display.flip()
