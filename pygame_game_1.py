import pygame as pg
import sys
import math


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def isInCircle(px, py, cx, cy, radius):
    dist = distance(px, py, cx, cy)
    if dist <= radius:
        return True

    return False


pg.init()

screenSize = 1000
screen = pg.display.set_mode((screenSize, screenSize * 0.8))
pg.display.set_caption('Click a button all day!')
pg.display.set_icon(pg.image.load(
    "C:\\Users\\asher\\OneDrive\\Documents\\Asher's Coding Folder\\Simple Game Javascript\\rahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.png"))
clock = pg.time.Clock()
mousePos = pg.mouse.get_pos()
mouseClicked = False

buttonFont = pg.font.SysFont(None, 12 * 4)
scoreFont = pg.font.SysFont(None, 12 * 5)
score = 0
click_processed = False
circleRectSize = 100

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    mouseClicked = pg.mouse.get_pressed()[0]

    pg.draw.circle(screen, (0, 0, 0),
                   ((screen.get_width() // 2), (screen.get_height() // 2) - 50), 100)
    pg.draw.circle(screen, (200, 0, 0),
                   ((screen.get_width() // 2), (screen.get_height() // 2) - 50), 98)
    pg.draw.circle(screen, (255, 0, 0),
                   ((screen.get_width() // 2), (screen.get_height() // 2) - 50), 78)
    buttonText = buttonFont.render("Click me!", True, (0, 0, 0))
    screen.blit(buttonText, ((screen.get_width() // 2) - 73, (screen.get_height() // 2) - 65))
    mousePos = pg.mouse.get_pos()
    scoreText = scoreFont.render("Score: " + str(score), True, (0, 255, 0))
    screen.blit(scoreText, ((screen.get_width() // 2) - 75, (screen.get_height() // 2) - 250))

    if isInCircle(mousePos[0], mousePos[1], screen.get_width() // 2, screen.get_height() // 2, 150):
        if mouseClicked and not click_processed:
            score += 1
            click_processed = True

    if not mouseClicked:
        click_processed = False

    # Run code if score is above or equal to 2500000.
    if score >= 2500000:
        winText = pg.font.Font(None, 159).render("You Win!", True, (255, 255, 0))
        screen.blit(winText, ((screen.get_width() // 2) - 390, (screen.get_height() // 1.5)))

    if pg.key.get_pressed()[pg.K_LEFTBRACKET]:
        score += 500

    if pg.key.get_pressed()[pg.K_RIGHTBRACKET]:
        score -= 500

    if pg.key.get_pressed()[pg.K_SLASH]:
        score += 5000

    if pg.key.get_pressed()[pg.K_BACKSPACE]:
        score -= 5000

    pg.display.flip()
