'''
Created on Mar 9, 2015

@author: emkess
'''

import pygame 
from pygame.locals import *
import sys

from UIUtils import Button

pygame.init()
pygame.font.init()

background = pygame.image.load("Instructions.png")
backgroundRect = background.get_rect()


size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Courier New', 20)
textBox = pygame.Rect((100, 100, 200, 300))

def load():
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 40
    
    RETURN_BUTTON_LOC = (0, 0)
    return_button = Button((255,255,255), "Buttons/Return.png", (RETURN_BUTTON_LOC[0],RETURN_BUTTON_LOC[1]))
   
#     GAMEPLAY_BUTTON_LOC = (50, 100)
#     gameplay_button = Button((255,255,255), "Buttons/GamePlay.png", (GAMEPLAY_BUTTON_LOC[0],GAMEPLAY_BUTTON_LOC[1]))
#     
    
    state = 1
    while( state == 1 ):
        screen.fill([255,255,255])
        screen.blit(background, backgroundRect)
        screen.blit(return_button.image, return_button)
#         screen.blit(gameplay_button.image, gameplay_button)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 0
            if event.type == MOUSEBUTTONDOWN:
                print("mouse click")
                loc = pygame.mouse.get_pos()
                
                '''
                Return Button Press
                
                '''
                if (return_button.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    return
                    
                #game play button press
#                 elif (loc[0] > GAMEPLAY_BUTTON_LOC[0] and loc[0] < (GAMEPLAY_BUTTON_LOC[0] + BUTTON_WIDTH) 
#                     and loc[1] > GAMEPLAY_BUTTON_LOC[1] and loc[1] < (GAMEPLAY_BUTTON_LOC[1] + BUTTON_HEIGHT)):
#                     print("game play screen")
#                     
                    #TODO load game play screen - do not use load() method
                    #because it will make another instance of the Instructions
                    #menu and you will have to click return twice to exit
                    #instructions - instead, make a new state (e.g. 3)
                    #to indicate viewing whatever information
                    state = 1
                else:
                    state = 1
        
     
         
        
# instructions_load()