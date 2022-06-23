#타원에 외접하는 직사각형을 지정하여 좌표 지정

import sys
import pygame
from pygame.locals import QUIT,Rect


pygame.init()
surface = pygame.display.set_mode((400,250))
fpsclock = pygame.time.Clock()

def main():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    surface.fill((255,255,255))

    #빨강
    pygame.draw.ellipse(surface, (255,0,0),(50,50,140,60))

    pygame.draw.ellipse(surface,(0,255,0),((250,130),(90,90)),20)

    pygame.display.update()
    fpsclock.tick(3)

if __name__ == '__main__':
    main()