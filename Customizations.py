'''
Created on Mar 9, 2015

@author: weismant
'''

import pygame 
from pygame.locals import *
import sys
import Image
from UIUtils import Button

pygame.init()
pygame.font.init()

background = pygame.image.load("res/background.png")
backgroundRect = background.get_rect()


size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Courier New', 20)
textBox = pygame.Rect((100, 100, 200, 300))

boat = 1

def load():
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 40
    
    RETURN_BUTTON_LOC = (0, 0 )
    return_button = Button((255,255,255), "Buttons/Return.png", (RETURN_BUTTON_LOC[0],RETURN_BUTTON_LOC[1]))
    
    BROWN_BOAT_LOC = (200, 0)
    brown_boat = Button((0,0,0), "res/boat.png", (BROWN_BOAT_LOC[0],BROWN_BOAT_LOC[1]), (150, 150))
   
    BLUE_BOAT_LOC = (200, 160)
    blue_boat = Button((255,255,255), "res/boatBlue.png", (BLUE_BOAT_LOC[0],BLUE_BOAT_LOC[1]), (150, 150))
   
    GREEN_BOAT_LOC = (0, 160)
    green_boat = Button((255,255,255), "res/boatGreen.png", (GREEN_BOAT_LOC[0],GREEN_BOAT_LOC[1]), (150, 150))
   
    RED_BOAT_LOC = (200, 320)
    red_boat = Button((255,255,255), "res/boatRed.png", (RED_BOAT_LOC[0],RED_BOAT_LOC[1]), (150, 150))
   
    YELLOW_BOAT_LOC = (0, 320)
    yellow_boat = Button((255,255,255), "res/boatYellow.png", (YELLOW_BOAT_LOC[0],YELLOW_BOAT_LOC[1]), (150, 150))
   
    
#     GAMEPLAY_BUTTON_LOC = (50, 100)
#     gameplay_button = Button((255,255,255), "Buttons/GamePlay.png", (GAMEPLAY_BUTTON_LOC[0],GAMEPLAY_BUTTON_LOC[1]))
#     
    
    state = 1
    while( state == 1 ):
        
        box_loc = (200, 0)
        box = Button((255,255,255), "res/check.png", (box_loc[0], box_loc[1]), (160, 160))
    
        screen.fill([255,255,255])
        screen.blit(background, backgroundRect)
        screen.blit(box.image, box)
        screen.blit(return_button.image, return_button)
        screen.blit(brown_boat.image, brown_boat)
        screen.blit(blue_boat.image, blue_boat)
        screen.blit(green_boat.image, green_boat)
        screen.blit(red_boat.image, red_boat)
        screen.blit(yellow_boat.image, yellow_boat)
        
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
                if (brown_boat.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    boat = 1
                    box_loc = BROWN_BOAT_LOC
                if (blue_boat.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    boat = 2
                    box_loc = BLUE_BOAT_LOC
                if (green_boat.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    boat = 3
                    box_loc = GREEN_BOAT_LOC
                if (red_boat.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    boat = 4
                    box_loc = RED_BOAT_LOC
                if (yellow_boat.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    boat = 5
                    box_loc = YELLOW_BOAT_LOC
                    
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
        