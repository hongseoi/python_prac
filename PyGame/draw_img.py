'''
이미지나 문자 출력은 선, 원처럼 명령어로 그릴 수 없다.
이미지, 문자는 Surface라는 영역에 그리고 Surface를 화면에 복사
'''
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((1000,400))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("hi.png")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((225,225,225))

        #blit(원본 surface이름, 좌표, 복사영역(일부만그릴때), 복사할때연산방법
        SURFACE.blit(logo,(20,50))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()