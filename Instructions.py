'''
Created on Mar 9, 2015

@author: emkess
'''

import pygame 
from pygame.locals import *

import Menu

pygame.init()
pygame.font.init()

background = pygame.image.load("res/InstructionBackground.png")
backgroundRect = background.get_rect()


size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

class Button(pygame.sprite.Sprite):
    def __init__(self, color, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (100,60))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

def load():
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 60
    RETURN_BUTTON_LOC = (250, 200)
    return_button = Button((255,255,255), "Buttons/Return.png", (RETURN_BUTTON_LOC[0],RETURN_BUTTON_LOC[1]))
    

    state = 1
    while( state == 1 ):
        screen.fill([255,255,255])
        screen.blit(return_button.image, return_button)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 0
            if event.type == MOUSEBUTTONDOWN:
                state = 2
                
    if (state == 2):
        print("mouse click")
        loc = pygame.mouse.get_pos()
        if (loc[0] > RETURN_BUTTON_LOC[0] and loc[0] < (RETURN_BUTTON_LOC[0] + BUTTON_WIDTH) 
            and loc[1] > RETURN_BUTTON_LOC[1] and loc[1] < (RETURN_BUTTON_LOC[1] + BUTTON_HEIGHT)):
            print("run game")
            Menu.menu()
        load()
            
        
# instructions_load()