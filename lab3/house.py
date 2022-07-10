import pygame
from pygame.draw import *

def main():
    x, y = 150, 400
    width, height = 200, 300

    pygame.init()
    FPS = 30
    screen = pygame.display.set_mode((500, 500))
    GREY = (180, 180, 180)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    house_foundation_color = BLACK
    house_walls_color = YELLOW
    house_roof_color = RED

    # Clear the screen and set the screen background
    screen.fill(GREY)

    draw_house(screen, house_foundation_color, house_walls_color, house_roof_color,
               x, y, width, height)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_house(screen, house_foundation_color, house_walls_color, house_roof_color,
               x, y, width, height):
    """
    Нарисовать домик ширины width и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x середины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамен или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    """
    print('Типа рисую домик...', x, y, width, height)
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(screen, house_foundation_color, x, y, width, foundation_height)
    draw_house_walls(screen, house_walls_color, x + 0.05 * width, y - walls_height, walls_width, walls_height)
    draw_house_roof(screen, house_roof_color, x, y - walls_height, width, roof_height)


def draw_house_foundation(screen, color, x, y, width, height):
    """
    Нарисовать основание домика ширины width и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x середины фундамента
    :param y: координата y низа фундамента
    :param width: полная ширина фундамена
    :param height: полная высота фундамента
    :return: None
    """
    rect(screen, color, (x, y, width, height))
    print('Типа рисую основание...', x, y, width, height)
    pass


def draw_house_walls(screen, color, x, y, width, height):
    rect(screen, color, (x, y, width, height))
    print('Типа рисую стены...', x, y, width, height)
    pass


def draw_house_roof(screen, color, x, y, width, height):
    pygame.draw.polygon(screen, color, [[x, y], [x + width, y], [x + 0.5 * width, y - height]])
    print('Типа рисую крышу...', x, y, width, height)
    pass


main()