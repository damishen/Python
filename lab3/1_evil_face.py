import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

GREY = (180, 180, 180)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Clear the screen and set the screen background
screen.fill(GREY)

circle(screen, (YELLOW), (200, 175), 100)
circle(screen, (BLACK), (200, 175), 100, 1)
# left eye
circle(screen, RED, (160, 160), 20)
circle(screen, BLACK, (160, 160), 20, 1)
circle(screen, BLACK, (160, 160), 7)
# right eye
circle(screen, RED, (230, 160), 15)
circle(screen, BLACK, (230, 160), 15, 1)
circle(screen, BLACK, (230, 160), 5)
# mouth
rect(screen, BLACK, (150, 230, 100, 20))
# left brow
pygame.draw.line(screen, BLACK, [100, 100], [180,140], 15)
# right brow
pygame.draw.line(screen, BLACK, [210, 140], [300,120], 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()