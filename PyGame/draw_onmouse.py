'''
마우스 입력: MOUSEBUTTIONDOWN
마우스 이동: MOUSEMOTION
마우스 해제: MOUSEBOTTONUP
'''

import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    mousepos = []
    mousedown = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                mousedown = True
            elif event.type == MOUSEMOTION:
                if mousedown:
                    mousepos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousedown = False
                mousepos.clear()

        SURFACE.fill((255,255,255))
        if len(mousepos) > 1:
            pygame.draw.lines(SURFACE, (255,0,0),False,mousepos)

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == "__main__":
    main()