import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((800, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 800)
    y = randint(100, 800)
    r = randint(100, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ((event.pos[0]-x)**2+(event.pos[1]-y)**2)**0.5 <= r:
                print('Попал!')
            else: print('Мимо!')

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()