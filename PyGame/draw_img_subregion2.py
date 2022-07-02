#이미지 여러개로 잘라서 사용하기

from itertools import count
import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT

pygame.init()
pygame.key.set_repeat(5,5)
SURFACE = pygame.display.set_mode((500,200))
FPSCLOCK = pygame.time.Clock()

def main():

    logo = pygame.image.load("hi.png")
    imgs = []

    for index in range(9):
        img = pygame.Surface((24,24))
        img.blit(logo,(0,0),Rect(index*24,0,24,24))
        imgs.append(img)

    counter = 0
    pos_x = 100
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pos_x -=5
                elif event.key == pygame.K_RIGHT:
                    pos_x += 5


        SURFACE.fill((0,0,0))
        SURFACE.blit(logo, (0,0))
        SURFACE.blit(logo, (250,50), Rect(50,50,100,100))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()