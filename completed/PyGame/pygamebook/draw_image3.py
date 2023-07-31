'''
이미지 회전: transform 클래스의 rotate 메소드 사용
변환값은 새로운 이미지의 surface 객체
rotate(surface, angle)
'''

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

        #logo 회전, 왼쪽 위가 (100,30)인 위치에 로고 그리기
        new_logo = pygame.transform.rotate(logo, theta)
        SURFACE.blit(new_logo, (100,30))

        pygame.display.update()
        FPSCLOCK.tick(30)
if __name__ == '__main__':
    main()