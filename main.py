import pygame
from components.uiElements import *
from elements.ui import *

pygame.init()
pygame.display.set_caption("PyLatro")
screen = pygame.display.set_mode((1460, 820))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont("monofetti", 20)

mousepos: tuple
mUp, mDown = False, False

buttons: list[Button] = getGameButtons()
containers: list[Container] = getContainers()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mUp = True

    mDown = pygame.mouse.get_pressed()[0]
    mousepos = pygame.mouse.get_pos()
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, "light gray", pygame.Rect(10, 10, 400, 800))

    for b in buttons:
        pygame.draw.rect(screen, "dark gray", b.getShadow())
        pygame.draw.rect(screen, b.getColor(), b.getRender())
        if b.isHovered(mousepos):
            if mUp:
                b.unpress()
                exec(b.command)
            if mDown:
                b.press()
        if mUp and b.pressed:
            b.unpress()

    for c in containers:
        pygame.draw.rect(screen, "light gray", c.getRender())

    mUp = False
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()