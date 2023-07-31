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

    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos, ypos = (x_pos+xoffset, y_pos+yoffset)
            if 0<= xpos < WIDTH and 0<= ypos < HEIGHT and field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENDED
                OPEN_COUNT += 1
            count = num_of_bombs(field,xpos,ypos)
            if count == 0 and not(xpos==x_pos and y_pos==y_pos):
                open_tile(field, xpos, ypos)

def main():
    '''메인루틴'''
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CREARED!!", True, (0,255,255))
    message_over = largefont.render("Game OVER", True, (0,255,255))
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)
    game_over = False
    
    field = [[EMPTY for xpos in range(WIDTH)]
             for ypos in range(HEIGHT)]
    
    #폭단 설치