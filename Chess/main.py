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
from Chess.Board import Board

pg.init()

bg_color = (183, 255, 183)
screen = Screen(pg, 800, 800).screen()
pg.display.set_icon(pg.image.load('chess-icon.png'))
pg.display.set_caption('Chess')


class Button:
    def __init__(self, x, y, w, h, text, font, color, hover_color):
        self.rect = pg.Rect(x, y, w, h)
        self.text = font.render(text, True, (0, 0, 0))
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse = pg.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse) else self.color
        pg.draw.rect(screen, current_color, self.rect, border_radius=8)
        text_rect = self.text.get_rect(center=self.rect.center)
        screen.blit(self.text, text_rect)

    def clicked(self):
        mouse = pg.mouse.get_pos()
        return self.rect.collidepoint(mouse) and pg.mouse.get_pressed()[0]


def exit_chess(code=0):
    pg.quit()
    sys.exit(code)


class Scene:
    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass


class TitleScene(Scene):
    def __init__(self):
        self.text_font = pg.font.SysFont('impact', 138)
        self.play_button = Button(320, 400, 175, 100, 'PLAY',
                                  pg.font.SysFont('', 72, True),
                                  (0, 255, 0), (0, 205, 0))
        self.quit_button = Button(320, 525, 175, 100, 'QUIT',
                                  pg.font.SysFont('', 72, True),
                                  (255, 0, 0), (205, 0, 0))

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                exit_chess()

        if self.play_button.clicked():
            return "game"

        if self.quit_button.clicked():
            exit_chess()

    def draw(self, screen):
        screen.fill(bg_color)

        # Draw title text
        chars = [self.text_font.render(i, False, (0, 0, 0) if 'Ches'.index(i) % 2 == 0 else (255, 255, 255))
                 for i in list('Ches')]
        chars.append(self.text_font.render('s', False, (0, 0, 0)))

        text_pos = (800 - sum(t.get_width() for t in chars)) // 2
        for t in chars:
            screen.blit(t, (text_pos, 300 - t.get_rect().centery))
            text_pos += t.get_width()

        # Draw buttons
        self.play_button.draw(screen)
        self.quit_button.draw(screen)


class GameScene(Scene):
    def __init__(self):
        self.board = Board((8, 8), screen, pg)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                exit_chess()

    def draw(self, screen):
        screen.fill(bg_color)
        self.board.draw(800, 800)


scenes = {
    "title": TitleScene(),
    "game": GameScene()
}

current_scene = "title"

while True:
    events = pg.event.get()

    next_scene = scenes[current_scene].handle_events(events)
    if next_scene:
        current_scene = next_scene

    scenes[current_scene].update()
    scenes[current_scene].draw(screen)

    pg.display.flip()
