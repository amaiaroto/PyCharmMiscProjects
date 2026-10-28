"""
Pong Game Implementation
A classic Pong game with adjustable difficulty levels and score tracking.
"""

# Importing stuff
import sys
import random
import time

import pygame

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


def getClick():
    return pygame.mouse.get_pressed()[0]


def getPos():
    return pygame.mouse.get_pos()


def quit():
    # print('quit')
    s.fill((0, 0, 0))
    pygame.time.wait(80)
    pygame.display.flip()

    for i in range(1, 4):
        pygame.display.set_caption('Closing' + ' .' * i)

        pygame.time.wait(1200 // 3)

    # print('quiting...')
    pygame.quit()
    sys.exit()


def play():
    # print('play')
    PONG.RUN()


def controls():
    # print('controls')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break  # go back to the menu

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            break

        s.fill((0, 0, 0))

        pygame.draw.circle(s, (150, 0, 0), (s.get_width() + r, s.get_height() - r), r)
        pygame.draw.circle(s, (255, 0, 0), (s.get_width() + r, s.get_height() - r), 80)

        backCircleRect = pygame.Rect(s.get_width(), s.get_height() - r, s.get_width() + r, s.get_height())

        pygame.draw.rect(s, (255, 255, 255), backCircleRect)

        exitText = fo.render('BACK', True, (255, 255, 255))
        exitTextRect = exitText.get_rect(center=(s.get_width() + r, s.get_height() - r))

        s.blit(exitText, exitTextRect)

        textcontrolsHeader = fo.render('\n\n\nMOVEMENT\n\n\n', True, (255, 255, 255))
        textcontrolsHeaderRect = textcontrolsHeader.get_rect(center=(s.get_width() / 2, s.get_height() / 2.5))

        textcontrols = fo.render('\nUP_KEY\n TO MOVE UP', True, (255, 255, 255))
        textcontrolsRect = textcontrols.get_rect(center=(s.get_width() / 2, s.get_height() / 2))

        textcontrols2 = pygame.font.Font(None, 17).render('\nDOWN_KEY\n TO MOVE DOWN', True, (255, 255, 255))
        textcontrols2Rect = textcontrols2.get_rect(center=((s.get_width() / 2) - pygame.font.Font(None, 17).get_height() + 10, s.get_height() / 2))

        s.blit(textcontrolsHeader, textcontrolsHeaderRect)
        s.blit(textcontrols, textcontrolsRect)

        if getClick():
            if backCircleRect.collidepoint(pygame.mouse.get_pos()):
                break # go back to the menu

        pygame.display.flip()


# Removing threads
if __name__ != '__main__':
    pygame.quit()
    sys.exit()

# Game startup
pygame.display.set_caption('Menu')

pygame.display.set_icon(pygame.image.load('GAME_LOGO-PONG.png'))

pygame.init()

PONG = GAME()

states = {
    'play': quit,
    'quit': play,
    'controls': controls,
    '': lambda: None
}

s = pygame.display.set_mode((1000, 800), pygame.FULLSCREEN)
fo = pygame.font.Font(None, 160)
fofo = pygame.font.Font(None, 318)

quite = pygame.event.custom_type()

while True:
    for event in pygame.event.get():
        if event.type == quite:
            pygame.quit()
            sys.exit()

    s.fill((0, 0, 0))

    r = s.get_width() / 10

    txet = fofo.render('PONG', True, (100, 100, 255))
    txetRect = txet.get_rect(center=(s.get_width() / 2, s.get_height() / 5))
    s.blit(txet, txetRect)

    circleQuitPos = (s.get_width() / 4, (s.get_height() / 2) - s.get_height() / 16)
    pygame.draw.circle(s, (150, 0, 0), circleQuitPos, r)
    pygame.draw.circle(s, (255, 0, 0), circleQuitPos, r - r / 10)
    t = fo.render('QUIT', True, (255, 255, 255))
    tRect = t.get_rect(center=circleQuitPos)
    circleQuitRect = pygame.rect.Rect((((circleQuitPos[0] - r), (circleQuitPos[1] - r), (r * 2), (r * 2))))
    s.blit(t, tRect)

    circlePlayPos = (s.get_width() / 2, (s.get_height() / 2) - s.get_height() / 16)
    pygame.draw.circle(s, (0, 150, 0), circlePlayPos, r)
    pygame.draw.circle(s, (0, 255, 0), circlePlayPos, r - r / 10)
    te = fo.render('PLAY', True, (255, 255, 255))
    teRect = te.get_rect(center=circlePlayPos)
    circlePlayRect = pygame.rect.Rect(((circlePlayPos[1] - r), (circlePlayPos[1] - r), (r * 2), (r * 2)))
    s.blit(te, teRect)

    circleControlsPos = ((s.get_width() / 4) * 3, (s.get_height() / 2) - s.get_height() / 16)
    pygame.draw.circle(s, (150, 150, 0), circleControlsPos, r)
    pygame.draw.circle(s, (255, 255, 0), circleControlsPos, r - r / 10)
    tx = fo.render('CONTROLS', True, (255, 255, 255))
    txRect = tx.get_rect(center=circleControlsPos)
    circleControlsRect = pygame.rect.Rect(((circleControlsPos[0] - r), (circleControlsPos[1] - r), (r * 2), (r * 2)))
    s.blit(tx, txRect)

    if getClick():
        # print('clicked')
        if circlePlayRect.collidepoint(getPos()):
            state = 'play'
            # print('clicked play')
            pygame.time.wait(200)

        elif circleQuitRect.collidepoint(getPos()):
            state = 'quit'
            # print('clicked quit')
            pygame.time.wait(200)

        elif circleControlsRect.collidepoint(getPos()):
            state = 'controls'
            # print('clicked controls')
            pygame.time.wait(200)

        else:
            state = ''
            # print('clicked nothing')
            pygame.time.wait(200)

    # try:
        # print(state[state.index(' ')])
    #
    # except ValueError:
        # print(bool(state.find(' ')))

    # print('state = ' + state)
    states[state]()
    state = ''

    pygame.display.flip()
