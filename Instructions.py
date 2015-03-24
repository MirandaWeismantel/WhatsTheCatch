'''
Created on Mar 9, 2015

@author: emkess
'''

import pygame 
from pygame.locals import *
import sys

pygame.init()
pygame.font.init()

background = pygame.image.load("res/InstructionBackground.png")
backgroundRect = background.get_rect()


size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Courier New', 20)
textBox = pygame.Rect((100, 100, 200, 300))




class Button(pygame.sprite.Sprite):
    def __init__(self, color, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (100,40))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

def load():
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 40
    
    TEXT_BOX = (150, 100)
    
    import Menu
    
    if (Menu.instructionsBox == 0):
        text_box = pygame.image.load("Buttons/text_box1.png")
        text_boxRect = text_box.get_rect()
        text_boxRect.x = TEXT_BOX[0]
        text_boxRect.y = TEXT_BOX[1]
        
    elif (Menu.instructionsBox == 1):
        text_box = pygame.image.load("Buttons/gameplay_text.png")
        text_boxRect = text_box.get_rect()
        text_boxRect.x = TEXT_BOX[0]
        text_boxRect.y = TEXT_BOX[1]
        
    elif (Menu.instructionsBox == 2):
        text_box = pygame.image.load("Buttons/controls_text.png")
        text_boxRect = text_box.get_rect()
        text_boxRect.x = TEXT_BOX[0]
        text_boxRect.y = TEXT_BOX[1]
    
    elif (Menu.instructionsBox == 3):
        text_box = pygame.image.load("Buttons/scoring_text.png")
        text_boxRect = text_box.get_rect()
        text_boxRect.x = TEXT_BOX[0]
        text_boxRect.y = TEXT_BOX[1]
    
    RETURN_BUTTON_LOC = (50, 400)
    return_button = Button((255,255,255), "Buttons/Return.png", (RETURN_BUTTON_LOC[0],RETURN_BUTTON_LOC[1]))
   
    GAMEPLAY_BUTTON_LOC = (50, 100)
    gameplay_button = Button((255,255,255), "Buttons/GamePlay.png", (GAMEPLAY_BUTTON_LOC[0],GAMEPLAY_BUTTON_LOC[1]))
    
    CONTROLS_BUTTON_LOC = (50, 200)
    controls_button = Button((255,255,255), "Buttons/Controls.png", (CONTROLS_BUTTON_LOC[0], CONTROLS_BUTTON_LOC[1]))
    
    SCORING_BUTTON_LOC = (50, 300)
    scoring_button = Button((255,255,255), "Buttons/Controls.png", (SCORING_BUTTON_LOC[0], SCORING_BUTTON_LOC[1]))
    
    state = 1
    while( state == 1 ):
        screen.fill([255,255,255])
        screen.blit(background, backgroundRect)
        screen.blit(text_box, text_boxRect)
        screen.blit(return_button.image, return_button)
        screen.blit(gameplay_button.image, gameplay_button)
        screen.blit(controls_button.image, controls_button)
        screen.blit(scoring_button.image, scoring_button)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 0
            if event.type == MOUSEBUTTONDOWN:
                state = 2
                
    if (state == 2):
        print("mouse click")
        loc = pygame.mouse.get_pos()
        
        '''
        Return Button Press
        
        '''
        if (loc[0] > RETURN_BUTTON_LOC[0] and loc[0] < (RETURN_BUTTON_LOC[0] + BUTTON_WIDTH) 
            and loc[1] > RETURN_BUTTON_LOC[1] and loc[1] < (RETURN_BUTTON_LOC[1] + BUTTON_HEIGHT)):
            print("run game")
            Menu.instructionsBox = 0
            Menu.menu()
            
        '''
        Game Play Button Press
        
        '''
        if (loc[0] > GAMEPLAY_BUTTON_LOC[0] and loc[0] < (GAMEPLAY_BUTTON_LOC[0] + BUTTON_WIDTH) 
            and loc[1] > GAMEPLAY_BUTTON_LOC[1] and loc[1] < (GAMEPLAY_BUTTON_LOC[1] + BUTTON_HEIGHT)):
            print("game play screen")
            Menu.instructionsBox = 1
            load()
        
        '''
        Controls Button Press
        
        '''
        if (loc[0] > CONTROLS_BUTTON_LOC[0] and loc[0] < (CONTROLS_BUTTON_LOC[0] + BUTTON_WIDTH) 
            and loc[1] > CONTROLS_BUTTON_LOC[1] and loc[1] < (CONTROLS_BUTTON_LOC[1] + BUTTON_HEIGHT)):
            print("controls screen")
            Menu.instructionsBox = 2
            load()
            
        '''
        Scoring Button Press
        
        '''    
        if (loc[0] > SCORING_BUTTON_LOC[0] and loc[0] < (SCORING_BUTTON_LOC[0] + BUTTON_WIDTH) 
            and loc[1] > SCORING_BUTTON_LOC[1] and loc[1] < (SCORING_BUTTON_LOC[1] + BUTTON_HEIGHT)):
            print("scoring screen")
            Menu.instructionsBox = 3
            load()
        
     
         
        
# instructions_load()