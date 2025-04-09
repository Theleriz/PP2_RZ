import pygame, sys
from pygame.locals import *
import random, time


FPS = 60
FramePerSec = pygame.time.Clock()


PIXEL_SIZE = 10
SCREEN_WIDHT = 400
SCREEN_HEIGHT  = 400

GRAY  = (180, 180, 180)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


screen = pygame.display.set_mode((SCREEN_WIDHT,SCREEN_HEIGHT))
screen.fill(BLACK)


def draw(x, y = 0):
    pygame.draw.rect(screen, GRAY, (x, y + PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))


def draw_angel(screen, x, y, index):
    radius = 10
    dx = x + random.randint(-2, 2)
    dy = y + random.randint(-2, 2)
    
    color = (random.randint(1, 2 ** index - 1), random.randint(1, 2 ** index - 1), random.randint(1, 2 ** index - 1) )

    pygame.draw.circle(screen, color, (x, y), 10)


while True:
    isBuffed = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    for i in range(1, 100):
        draw_angel(screen, 200, 200, i)
        time.sleep(1)
   

    pygame.display.update()
    FramePerSec.tick(FPS)

