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


background1 = pygame.image.load("pdf2png/Instructions1/Instructions1-1.png")
backgroundRect1 = background1.get_rect()

background2 = pygame.image.load("pdf2png/Instructions2/Instructions2-1.png")
backgroundRect2 = background2.get_rect()

background3 = pygame.image.load("pdf2png/Instructions3/Instructions3-1.png")
backgroundRect3 = background3.get_rect()

background4 = pygame.image.load("pdf2png/Instructions4/Instructions4-1.png")
backgroundRect4 = background4.get_rect()

background5 = pygame.image.load("pdf2png/Instructions5/Instructions5-1.png")
backgroundRect5 = background5.get_rect()


size = (width, height) = background1.get_size()
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Courier New', 20)
textBox = pygame.Rect((100, 100, 200, 300))

def load():
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 40
    
    RETURN_BUTTON_LOC = (200, 0)
    return_button = Button((255,255,255), "Buttons/Return.png", (RETURN_BUTTON_LOC[0],RETURN_BUTTON_LOC[1]))
    
    NEXT_BUTTON_LOC = (400, 0)
    next_button = Button((255,255,255), "Buttons/NextButton.png", (NEXT_BUTTON_LOC[0],NEXT_BUTTON_LOC[1]))
    
    PREV_BUTTON_LOC = (0, 0)
    prev_button = Button((255,255,255), "Buttons/BackButton.png", (PREV_BUTTON_LOC[0],PREV_BUTTON_LOC[1]))
    
    
    page = 1
   
#     GAMEPLAY_BUTTON_LO = (50, 100)
#     gameplay_button = Button((255,255,255), "Buttons/GamePlay.png", (GAMEPLAY_BUTTON_LOC[0],GAMEPLAY_BUTTON_LOC[1]))
#     
    
    state = 1
    while( state == 1 ):
        screen.fill([255,255,255])
        if (page == 1):
            screen.blit(background1, backgroundRect1)
            screen.blit(next_button.image, next_button)
            
        if (page == 2):
            screen.blit(background2, backgroundRect2)
            screen.blit(next_button.image, next_button)
            screen.blit(prev_button.image, prev_button)
            
        if (page == 3):
            screen.blit(background3, backgroundRect3)
            screen.blit(next_button.image, next_button)
            screen.blit(prev_button.image, prev_button)
            
        if (page == 4):
            screen.blit(background4, backgroundRect4)
            screen.blit(next_button.image, next_button)
            screen.blit(prev_button.image, prev_button)
            
            
        if (page == 5):
            screen.blit(background5, backgroundRect5)
            screen.blit(prev_button.image, prev_button)
        
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
                if (next_button.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    page = page + 1
                    if (page > 5):
                        page = 5
                if (prev_button.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    page = page - 1
                    if (page < 1):
                        page = 1
                    
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