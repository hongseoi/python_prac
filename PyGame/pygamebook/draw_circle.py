import sys
from turtle import update
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
surface = pygame.display.set_mode((400,300))
fpsclock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        surface.fill((255,255,255))

        #빨간색 꽉채워서
        pygame.draw.circle(surface,(255,0,0),(50,50),20)

        #빨강 굵기 10
        pygame.draw.circle(surface, (255,0,0), (150, 50), 20, 10)

        #녹색 반경 10
        pygame.draw.circle(surface,(0,255,0),(150,150),10)

        pygame.draw.circle(surface,(0,255,0),(150,250),10)

        pygame.display,update()
        fpsclock.tick(3)

if __name__ == "__main__":
    main()