import sys
from turtle import end_poly
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,200))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))

        pygame.draw.line(SURFACE,(255,0,0),(10,80),(200,80))

        #녹색 빗금 굵기 10
        start_pos = (300,30)
        end_pos = (380, 200)
        pygame.draw.line(SURFACE, (0,0,255), start_pos,end_pos,10)

        #for문을 이용해 격자 모양 무늬 그리기
        ## 하얀색 세로줄
        for xpos in range(0,400,25):
            pygame.draw.line(SURFACE, 0xFFFFFF, (xpos,0),(xpos,300))

        #하얀색 세로줄
        for ypos in range(0,300,25):
            pygame.draw.line(SURFACE, 0xFFFFFF,(0,ypos),(400,ypos))

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()
