'''
이미지 서플리션
blit 인수에 영역 지정해 이미지 일부만 그리기
'''
import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((500,200))
FPSCLOCK = pygame.time.Clock()

def main():

    logo = pygame.image.load("hi.png")
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((225,225,225))
        SURFACE.blit(logo, (0,0))
        SURFACE.blit(logo, (250,50), Rect(50,50,100,100))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()