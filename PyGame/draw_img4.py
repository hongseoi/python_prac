'''
이미지를 중심 축으로 회전하는 코드
'''
from cmath import rect
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("hi.png")
    theta = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        theta += 1

        SURFACE.fill((225,225,225))

        #logo 회전, 중심이 (200,150)인 위치에 로고 그리기
        new_logo = pygame.transform.rotate(logo, theta)
        rect.center = (200,150)
        SURFACE.blit(new_logo, rect)

        pygame.display.update()
        FPSCLOCK.tick(30)
if __name__ == '__main__':
    main()