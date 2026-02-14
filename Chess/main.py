# Credits and Attributes
# credit to rizal2109 on flaticon.com for chess-icon.png
# credit to all the authors of the unused assets

import os
import sys
from contextlib import redirect_stdout

with redirect_stdout(open(os.devnull, 'w')):
    import pygame as pg

from Chess.Screen import Screen
from Chess.Pieces import Piece

pg.init()

screen = Screen(pg, 800, 800).screen()
pg.display.set_icon(pg.image.load('chess-icon.png'))
pg.display.set_caption('Chess')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((200, 255, 200))

    # text = pg.font.SysFont(None, 138, True)
    # chars = [text.render(i, False, (0, 0, 0) if 'Ches'.index(i) % 2 == 0 else (255, 255, 255)) for i in list('Ches')]
    # chars.append(text.render('s', False, (0, 0, 0)))
    #
    # a = 400 - text.render('', True, (0,0,0)).get_size()[0] * len('Chess')
    # for t in chars:
    #     screen.blit(t, (a - t.get_rect().centerx, 300 - t.get_rect().centery))
    #     a += t.get_size()[0]

    pg.display.flip()
