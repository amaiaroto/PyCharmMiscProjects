import colorsys

import pygame as pg


class Line:
    def __init__(self,
                 start_color: tuple[int, int, int] | list[int],
                 start_pos: list[int | float],
                 end_pos: list[int | float],
                 surface: pg.SurfaceType,
                 width: int = 1,
                 pygame=pg) -> None:
        """
        A line, used for pygame drawing.
        :param start_color: RGB value. e.g: [255, 0, 255]
        :param start_pos: XY pos
        :param end_pos: XY pos
        :param surface: the surface to display the line
        :param width: the width of the line
        :param pygame: the pygame object
        """

        self.color = start_color
        self.start = start_pos
        self.end = end_pos
        self.surface = surface
        self.width = width
        self.hue = 0
        self.pygame = pygame

    def _calculate_color(self) -> list[int]:
        """
        Calculate the color of the line and change it.
        """

        self.hue += 1
        self.color = [int(v * 255) for v in colorsys.hsv_to_rgb((self.hue % 360) / 360, 1.0, 1.0)]

        return self.color

    def move(self,
             start_delta_x: int | float,
             start_delta_y: int | float,
             end_delta_x: int | float,
             end_delta_y: int | float):
        """
        Move the start and end of the line.
        :param start_delta_x: the amount of pixels to move the start pos horizontally
        :param start_delta_y: the amount of pixels to move the start pos vertically
        :param end_delta_x: the amount of pixels to move the end pos horizontally
        :param end_delta_y: the amount of pixels to move the end pos vertically
        """

        self.start[0] += start_delta_x
        self.start[1] += start_delta_y

        self.end[0] += end_delta_x
        self.end[1] += end_delta_y

    def draw(self) -> None:
        """
        Draw the line on the surface.
        """

        self._calculate_color()
        self.pygame.draw.line(self.surface, self.color, self.start, self.end, self.width)


screen: pg.Surface = pg.display.set_mode((1200, 800))
color: tuple[int, int, int] = (0, 0, 0)
lines: list[Line] = []
speed: int = -2

if __name__ == '__main__':
    pg.init()

    pg.display.set_caption("Satifying Rainbow Effect")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        screen.fill(color)

        lines.append(Line([0, 0, 0], [1200, 0], [1600, 800], screen, 5))

        for line in lines:
            line.move(speed, 0, speed, 0)
            line.draw()

        if len(lines) >= 820:
            speed = -speed

        pg.display.flip()
