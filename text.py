# Source - https://stackoverflow.com/a/60988595
# Posted by Rabbid76, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-12, License - CC BY-SA 4.0

import pygame
import pygame.font

pygame.init()

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
textRect = pygame.Rect(0, 0, 0, 0)

def text(font : str='', size : int=12, text : str='arial.ttf', color=(), x=0, y=0, bold : bool=True, outline: int=2):
    global textRect, textSurf
    # font = pygame.font.Font(font,size)
    font = pygame.font.SysFont(None, size)
    font.set_bold(True)
    if outline > 0:
        outlineSurf = font.render(text, True, (248, 234, 191))
        outlineSize = outlineSurf.get_size()
        if outline > 0:
            outlineSurf = font.render(text, True, (248, 234, 191))
            ow, oh = outlineSurf.get_size()

            textSurf = pygame.Surface((ow + outline * 2, oh + outline * 2), pygame.SRCALPHA)

            offsets = [
                (ox, oy)
                for ox in range(-outline, outline + 1)
                for oy in range(-outline, outline + 1)
                if ox != 0 or oy != 0
            ]

            cx, cy = (ow // 2 + outline, oh // 2 + outline)

            for ox, oy in offsets:
                textSurf.blit(outlineSurf, outlineSurf.get_rect(center=(cx + ox, cy + oy)))

            innerText = font.render(text, True, color)
            textSurf.blit(innerText, innerText.get_rect(center=(cx, cy)))

        textRect = textSurf.get_rect()
        offsets = [(ox, oy)
            for ox in range(-outline, 2*outline, outline)
            for oy in range(-outline, 2*outline, outline)
            if ox != 0 or ox != 0]
        for ox, oy in offsets:
            px, py = textRect.center
            textSurf.blit(outlineSurf, outlineSurf.get_rect(center = (px+ox, py+oy)))
        innerText = font.render(text, True, color).convert_alpha()
        textSurf.blit(innerText, innerText.get_rect(center = textRect.center))
    else:
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect()

    textRect.center = (x,y)
    screen.blit(textSurf, textRect)

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    hover = textRect.collidepoint(pygame.mouse.get_pos())
    outlineSize = 1 if hover else 0

    screen.fill((0,255,0))
    text('arial.ttf', 40, 'P', (0, 0, 0), (width / 2), (height / 2), True, outlineSize)
    pygame.display.flip()
