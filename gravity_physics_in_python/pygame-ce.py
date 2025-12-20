import pygame as pg
import sys
import colorsys
import random

pg.init()


class RainbowCircle:
    def __init__(self, radius: int = 400, layers: int = 6, colors: list[tuple[int, int, int] | str] | None = None):
        # if colors is None:
        # options = [((i, [r for r in range(256)]) for _ in range(256)) for i in range(256)]
        # colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        # if round(random.random()):
        #     colors = ["white", "gray", (50, 50, 50), "black"]
        #

        self.radius = radius
        self.layers = layers
        self.colors = colors
        self.times = 40

    def draw(self, screenObject, pygameObject, position: tuple[int, int] | None = None):
        if position is None:
            position = (screenObject.get_width() // 2, screenObject.get_height() // 2)
        # global screen
        # color=list()
        h = 0  # random.random()
        delta = 1.0 / self.layers
        radius = self.radius
        delta_radius = radius / self.layers
        for _ in range(self.layers):
            color = colorsys.hsv_to_rgb(h, 1, 1)
            color=list(map(lambda v: int(v*255),color))
            pygameObject.draw.circle(screenObject, color, position, radius)
            radius -= delta_radius
            h += delta
            # print(h)

        #
        # #h is a number from 0 to 1
        # #divide 1 by layers, that gives you the delta color between each layer of the rainbow
        # #loop over 0 to layers-1 and then start with h=0 and for each iteration do a h+=the delta at the previous step
        # #then call hsv to rgb
        # 2736, 1824
        #
        # for 'a' in range(len(self.colors)):
        #     pygameObject.draw.circle(screenObject, self.colors[a], position, self.radius)
        #     self.times -= 1 if self.times > 0 else 0
        #     self.radius -= 0.75 if self.radius > 0 else 0


screen = pg.display.set_mode((1000, 800))
rainbow = RainbowCircle(layers=5)
i = 1
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if pg.key.get_pressed()[pg.K_ESCAPE] or pg.key.get_pressed()[pg.K_DELETE]:
        pg.quit()
        sys.exit()
    screen.fill((255, 255, 255))

    rainbow.draw(screen, pg)
    # pg.draw.circle(scree)

    pg.display.flip()
