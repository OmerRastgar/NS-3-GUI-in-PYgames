import pygame
from pygame.locals import *
import subprocess
import os
RED = (255, 0, 0)
GRAY = (150, 150, 150)
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
BLUE = pygame.Color('lightblue')

pygame.init()
pygame.display.set_caption('LTE Vulnerability Test Environment')
icon = pygame.image.load("lteicon.png")
pygame.display.set_icon(icon)
w, h = 750, 800


    

def main():
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    running = True
    imp = pygame.image.load("map.jpg").convert()
    imp = pygame.transform.scale(imp,(w,h))
    
    
    play__img = pygame.image.load('play-button.png')
    play__img = pygame.transform.scale(play__img,(80,80))
    play__img.convert()
    stop__img = pygame.image.load('stop-button.png')
    stop__img = pygame.transform.scale(stop__img,(80,80))
    stop__img.convert()
    
    msg_img = pygame.image.load('wireless.png')
    msg_img = pygame.transform.scale(msg_img,(700,700))
    msg_img.convert()
    


    msg = msg_img.get_rect()
    msg.center = 10, 720
    play = play__img.get_rect(topleft=(10, 720))
    stop = stop__img.get_rect(center=(700, 50))
    stop2 = stop__img.get_rect(center=(50, 50))
    panel = pygame.rect.Rect(0,0,w//8,h)
    TOPpanel = pygame.rect.Rect(200,5,w//2,h//16)
    x=0
    y=0
    count = False
    hh=0
    

        

    while running:

        for event in pygame.event.get():
            

            
            if event.type == QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                count=1
       
        
            
        

            
        
        screen.fill(GRAY)
        #panel
        screen.blit(imp, (0, 0))
        pygame.draw.rect(screen, GRAY, panel)
        pygame.draw.rect(screen, GRAY, TOPpanel)
        #icon
       
        screen.blit(play__img, play)
        pygame.draw.rect(screen, GRAY, play,1)
        screen.blit(stop__img, stop)
        pygame.draw.rect(screen, GRAY, stop,1)
        screen.blit(stop__img, stop2)
        pygame.draw.rect(screen, GRAY, stop,1)
        msg.bottom= play.x,play.y
        msg.top=stop.x,stop.y
        screen.blit(msg_img,msg )
        pygame.draw.rect(screen, GRAY, msg,1)
        clock.tick(24)

        pygame.display.update()
        
            

    pygame.quit()

main()