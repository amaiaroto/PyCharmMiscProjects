import pygame as pg

from pieces_ import Pieces

pg.init()

screenSize = 800
padding = 0
spaceSize = 0
screen = pg.display.set_mode((screenSize, screenSize), pg.RESIZABLE)
board: dict = {
    'text_pos': {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None},
    'b': {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None},
    'c': {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None},
    'd': {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None},
    'e': {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None},
    'f': {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None},
    'g': {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None},
    'h': {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None}
}
ChessPieces = Pieces(board)

isRunning = True


# todo function to draw text_pos checkboard:
# -lopp over the column
#     loop over the row
# if color black else white
#         place text_pos square at (c*size,r*size) ((c+1)*size),((r+1)*size))
#         alternate the fill color
#         color=not color
# ()

#    pg.draw.rect(screen, (0, 0, 0), pg.Rect(padding, padding, spaceSize - padding, spaceSize - padding))
#    pg.draw.rect(screen, (200, 255, 200),
#                pg.Rect(padding + 12, padding + 12, spaceSize*0.9, spaceSize*0.9))

def draw_board():
    color = False
    for c in range(1, 9):
        for r in range(1, 9):
            pg.draw.rect(screen, (0, 0, 0) if color else (255, 255, 255),
                         (c * spaceSize, r * spaceSize, (c + 1) * spaceSize, (r + 1) * spaceSize))
            color = not color

while isRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
            continue

    padding = screenSize // 5
    spaceSize = screenSize - padding
    screen.fill((200, 255, 200))

    draw_board()

    pg.display.flip()

pg.quit()
