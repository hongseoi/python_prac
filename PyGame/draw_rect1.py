from mimetypes import suffix_map
import py_compile

import pygame
import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
surface = pygame.display.set_mode((300,400))
fpsclock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        surface.fill((255,255,255))

        #꽉 채워 칠하기
        pygame.draw.rect(surface, (255,0,0),(10,20,100,50))

        #굵기3
        pygame.draw.rect(surface, (255,0,0),(150,100,200,30),3)

        #직사각형
        pygame.draw.rect(surface, (0,255,0), ((100,80),(80,50)))

        #직사각형 rect 객체
        rect0 = Rect(200,60,140,80)
        pygame.draw.rect(surface,(0,0,255),rect0)

        pygame.display.update()
        fpsclock.tick(3)

if __name__ == '__main__':
    main()
