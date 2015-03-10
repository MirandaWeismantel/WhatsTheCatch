'''
Created on Mar 3, 2015

@author: emkess
'''

import pygame 
from pygame.locals import *

import Tester
import Instructions 


pygame.init()
pygame.font.init()

background = pygame.image.load("res/background.png")
backgroundRect = background.get_rect()


size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)


class Button(pygame.sprite.Sprite):
    def __init__(self, color, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
    
     
        
def menu():

    newGame = Button((255,255,255), "res/testButton.png", (50,50))
    instructions = Button((255,255,255), "res/testButton.png", (100,50))
    
    state = 0
    while state == 0:
        screen.fill([255,255,255])
        screen.blit(newGame.image, newGame)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
            elif event.type == MOUSEBUTTONDOWN:
                state = 2
            
    if (state == 2):
        print("mouse click")
        loc = pygame.mouse.get_pos()
        if (loc[0] > 50 and loc[0] < 90 and loc[1] > 50 and loc[1] < 90):
            print("main game")
            Tester.mainGame()
#         if (loc[0] > 100 and loc[0] < 140 and loc[1] > 50 and loc[1] < 90):
#             print("instructions")
#             Instructions.instructions_load()
        menu()

            
        
menu()