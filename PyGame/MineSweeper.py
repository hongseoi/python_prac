import sys
import pygame
from math import floor
from random import randint
from pygame.locals import QUIT, MOUSEBUTTONDOWN

WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 1
OPENDED =2
OPEN_COUNT = 0
CHECKED = [0 for _ in range(WIDTH) for _ in range(HEIGHT)]

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])
FPSCLOCK = pygame.time.Clock()

def num_of_bombs(field, x_pos, y_pos):
    #주위에 있는 폭탄 수 반환
    count = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1,2):
            xpos, ypos = (x_pos+xoffset, y_pos+yoffset)
            if 0<=xpos<WIDTH and 0<=ypos<HEIGHT and field[ypos][xpos]==BOMB:
                count+=1
    return count

def open_tile(field, x_pos, y_pos):
    # 타일 오픈
    global OPEN_COUNT
    if CHECKED[y_pos][x_pos]:
        return
    CHECKED[y_pos][x_pos] = True

    for 