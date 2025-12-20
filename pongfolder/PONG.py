"""
Pong Game Implementation
A classic Pong game with adjustable difficulty levels and score tracking.
"""

# Importing stuff
import sys
import random
import time

import pygame as pg

try:
    from PADDLE import PADDLE
    from BALL import BALL
    from GAME import GAME
    from GAME_CONFIG import GameConfig
    from SCORE import SCORE

except Exception as e:
    print(e)

flag = False
state = ''


def align_text(x, y, width, height, text: str, justifacation, screen: pg.Surface):
    lines = text.split('\n', 12)
    lens_of_lines = [len(i) for i in lines]
    screen.blit(pg.Surface(pg.rect.Rect(x, y, width, height)), (x, y))


def getClick():
    return pg.mouse.get_pressed()[0]


def getPos():
    return pg.mouse.get_pos()


def G_quit():
    # print('quit')
    s.fill((0, 0, 0))
    # pg.time.wait(80)
    pg.display.flip()

    # for i in range(1, 4):
    #     pg.display.set_caption('Closing' + ' .' * i)
    #
    #     pg.time.wait(1200 // 3)

    # print('quiting...')
    pg.quit()
    sys.exit()


def play():
    # print('play')
    PONG.RUN()


def controls():
    # print('controls')
    while True:
        for events in pg.event.get():
            if events.type == pg.QUIT:
                break  # go back to the menu

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            break

        s.fill((0, 0, 0))

        pg.draw.circle(s, (150, 0, 0), (s.get_width() + r, s.get_height() - r), r)
        pg.draw.circle(s, (255, 0, 0), (s.get_width() + r, s.get_height() - r), 80)

        backCircleRect = pg.Rect(s.get_width(), s.get_height() - r, s.get_width() + r, s.get_height())

        pg.draw.rect(s, (255, 255, 255), backCircleRect)

        exitText = fo.render('BACK', True, (255, 255, 255))
        exitTextRect = exitText.get_rect(center=(s.get_width() + r, s.get_height() - r))

        s.blit(exitText, exitTextRect)

        textcontrolsHeader = fo.render('MOVEMENT', True, (255, 255, 255))
        textcontrolsHeaderRect = textcontrolsHeader.get_rect(center=(s.get_width() / 2, s.get_height() / 2.5))

        textcontrols = fo.render('UP_KEY TO MOVE UP', True, (255, 255, 255))
        textcontrolsRect = textcontrols.get_rect(center=(s.get_width() / 2, s.get_height() / 2))

        textcontrols2 = fo.render('DOWN_KEY TO MOVE DOWN', True, (255, 255, 255))
        textcontrols2Rect = textcontrols2.get_rect(
            center=((s.get_width() / 2) - fo.get_height() + 20, s.get_height() / 1.75))

        s.blit(textcontrolsHeader, textcontrolsHeaderRect)
        s.blit(textcontrols, textcontrolsRect)
        s.blit(textcontrols2, textcontrols2Rect)

        if getClick():
            if backCircleRect.collidepoint(pg.mouse.get_pos()):
                break  # go back to the menu

        pg.display.flip()


# amiairoto
# Removing threads
if __name__ != '__main__':
    pg.quit()
    sys.exit()

# Game startup
pg.display.set_caption('Menu')

pg.display.set_icon(pg.image.load('GAME_LOGO-PONG.png'))

pg.init()

PONG = GAME()

states = {
    'play': G_quit,
    'quit': play,
    'controls': controls,
    '': lambda: None
}

s = pg.display.set_mode((1000, 800), pg.FULLSCREEN)
default_font_size = round(160 // 1.5)
header_font_size = round(318 // 1.5)
fo = pg.font.Font(None, default_font_size)
fofo = pg.font.Font(None, header_font_size)

quite = pg.event.custom_type()

while True:
    for event in pg.event.get():
        if event.type == quite:
            pg.quit()
            sys.exit()

    s.fill((0, 0, 0))

    r = s.get_width() / 10

    txet = fofo.render('PONG', True, (100, 100, 255))
    txetRect = txet.get_rect(center=(s.get_width() / 2, s.get_height() / 5))
    s.blit(txet, txetRect)

    circleQuitPos = (s.get_width() / 4, (s.get_height() / 2) - s.get_height() / 16)
    pg.draw.circle(s, (150, 0, 0), circleQuitPos, r)
    pg.draw.circle(s, (255, 0, 0), circleQuitPos, r - r / 10)
    t = fo.render('QUIT', True, (255, 255, 255))
    tRect = t.get_rect(center=circleQuitPos)
    circleQuitRect = pg.rect.Rect(((circleQuitPos[0] - r), (circleQuitPos[1] - r), (r * 2), (r * 2)))
    s.blit(t, tRect)

    circlePlayPos = (s.get_width() / 2, (s.get_height() / 2) - s.get_height() / 16)
    pg.draw.circle(s, (0, 150, 0), circlePlayPos, r)
    pg.draw.circle(s, (0, 255, 0), circlePlayPos, r - r / 10)
    te = fo.render('PLAY', True, (255, 255, 255))
    teRect = te.get_rect(center=circlePlayPos)
    circlePlayRect = pg.rect.Rect(((circlePlayPos[1] - r), (circlePlayPos[1] - r), (r * 2), (r * 2)))
    s.blit(te, teRect)

    circleControlsPos = ((s.get_width() / 4) * 3, (s.get_height() / 2) - s.get_height() / 16)
    pg.draw.circle(s, (150, 150, 0), circleControlsPos, r)
    pg.draw.circle(s, (255, 255, 0), circleControlsPos, r - r / 10)
    tx = fo.render('CTRLS', True, (255, 255, 255))
    txRect = tx.get_rect(center=circleControlsPos)
    circleControlsRect = pg.rect.Rect(((circleControlsPos[0] - r), (circleControlsPos[1] - r), (r * 2), (r * 2)))
    s.blit(tx, txRect)

    if getClick():
        # print('clicked')
        if circlePlayRect.collidepoint(getPos()):
            state = 'play'
            # print('clicked play')
            pg.time.wait(200)

        elif circleQuitRect.collidepoint(getPos()):
            state = 'quit'
            # print('clicked quit')
            pg.time.wait(200)

        elif circleControlsRect.collidepoint(getPos()):
            state = 'controls'
            # print('clicked controls')
            pg.time.wait(200)

        else:
            state = ''
            # print('clicked nothing')
            pg.time.wait(200)

    # try:
    # print(state[state.index(' ')])
    #
    # except ValueError:
    # print(bool(state.find(' ')))

    # print('state = ' + state)
    states[state]()
    state = ''

    pg.display.flip()
