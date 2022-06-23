import sys
import pygame
from pygame.locals import QUIT

pygame.init() #pygame 모듈 초기화
SURFACE = pygame.display.set_mode((400,300)) #크기 지정 후 변수에 저장
pygame.display.set_caption("just window") #윈도우 타이틀 설정

def main():
    while True:
        SURFACE.fill((255,255,0)) #윈도우 색 흰색(255,255,255)

        for event in pygame.event.get(): #종료 처리가 이뤄질 때까지 루프 지속. 이벤트 큐에서 이벤트 읽고 event 변수에 저장.
            if event.type == QUIT:
                pygame.quit() #pygame 초기화 해제
                sys.exit() #프로그램 종료
        pygame.display.update() #프로그램 내에서 그린 내용 반영

if __name__ == "__main__":
    main()