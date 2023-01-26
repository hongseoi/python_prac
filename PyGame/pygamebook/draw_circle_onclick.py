'''
pygame을 이용한 이벤트 처리
1. 마우스 클릭 by MOUSEBUTTIONDOWN

event.pos >> 마우스 좌표를 (x, y) 튜플 형태로 리턴. 이걸 append 함수를 이용해 리스트에 추가.
'''

import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    mousepos = []

    while True:
        SURFACE.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                mousepos.append(event.pos)
        
        for pos in mousepos:
            pygame.draw.circle(SURFACE, (0,255,0),pos, 5)

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == "__main__":
    main()