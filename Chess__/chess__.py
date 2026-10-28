import pygame as pg
from pieces__ import *

# plan for 2/12
# implementing valid moves
# finish to iniialize the board
# fix minor problem
# implement turn
# click to select piece, click to select target location


# remove, use the board instead to get the position of the pieces
alphabet = ["", "text_pos", "b", "c", "d", "e", "f", "g", "h"]

pg.init()

hover, rects = False, []
mousepos = pg.mouse.get_pos()
screenSize = 800
padding = 0
spaceSize = 0
screen = pg.display.set_mode((screenSize, screenSize), pg.RESIZABLE)
board = {}
pg.display.set_icon(pg.image.load("perfect__king.png"))
pg.display.set_caption("Chess__")

ChessPieces = Board()

# remove, do not use eval. that opens you up to injection of code
# use the json library to initialize your boar
ChessPieces.board = eval(open('startingboard__.json', 'r').read())

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

# move it as text_pos method of the board class
def draw_board(state, width, height, rows=8, columns=8, uc='w'):
    global textSurf, hover, rects
    rects = []

    try:
        squareSize = min(width, height) // (max(rows, columns) + 2)
        for r in range(1, columns + 1):
            for c in range(1, rows + 1):
                pg.draw.rect(screen, (0, 0, 0) if (r + c) % 2 == 0 else (255, 255, 255),
                             (squareSize * c, squareSize * r, squareSize, squareSize))
                if state[alphabet[c]][str(r)]:
                    text_font = pg.font.SysFont('Arial', squareSize, False)
                    text_font2 = pg.font.SysFont('Arial', squareSize, True)
                    text = text_font.render(state[alphabet[c]][str(r)].split(':')[1].upper(), True,
                                            (205, 205, 205) if state[alphabet[c]][str(r)].split(':')[
                                                                   0].lower() == uc else (80, 80,
                                                                                          80))
                    text2 = text_font2.render(state[alphabet[c]][str(r)].split(':')[1].upper(), True,
                                              (201, 159, 77))
                    rects.append(text2.get_rect())
                    if hover:
                        screen.blit(text2, (squareSize * c, squareSize * r))
                    screen.blit(text, (squareSize * c, squareSize * r))

    except IndexError as e:
        exit(f'{e}: square not valid')


while isRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
            continue

    screen.fill((200, 255, 200))
    mousepos = pg.mouse.get_pos()
    for r in rects:
        if r.collidepoint(mousepos):
            hover = True
            break

        else:
            hover = False

    draw_board(ChessPieces.board, screen.get_width(), screen.get_height())

    pg.display.flip()

pg.quit()
