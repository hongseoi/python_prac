import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock() #클럭 객체 작성후 변수에 저장

def main():
    sysfont = pygame.font.SysFont(None,36)
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        counter += 1
        SURFACE.fill((0,0,0))
        count_image = sysfont.render("count is {}".format(counter),True,(255,255,255))
        SURFACE.blit(count_image,(50,50))
        pygame.display.update()
        FPSCLOCK.tick(10) #적절한 휴식 취할 수 있도록 1초에 10회 루프되도록 지정 >> cpu 사용량 감소

if __name__ == "__main__":
    main()