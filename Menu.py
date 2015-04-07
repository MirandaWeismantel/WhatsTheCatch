'''
Created on Mar 3, 2015

@author: emkess
'''

import pygame 
from pygame.locals import *

import Tester
import Instructions
import sys
from UIUtils import Button

pygame.init()
pygame.font.init()

background = pygame.image.load("res/MenuBackground.png")
backgroundRect = background.get_rect()


size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

instructionsBox = 0
        
def menu():
    PLAY_BUTTON_LOCATION = (100, 240)
    INSTRUCTION_BUTTON_LOCATION = (300, 240)
    newGame = Button((255,255,255), "Buttons/PlayButton.png", (PLAY_BUTTON_LOCATION))
    instructions = Button((255,255,255), "Buttons/InstructionButton.png", (INSTRUCTION_BUTTON_LOCATION))
    
    Tester.restart()
    
    state = 0
    while state == 0:
        screen.fill([255,255,255])
        screen.blit(background, backgroundRect)
        screen.blit(newGame.image, newGame)
        screen.blit(instructions.image, instructions)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit("quit game")
            if event.type == MOUSEBUTTONDOWN:
                print("mouse click")
                loc = pygame.mouse.get_pos()
                if (newGame.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    print("main game")
                    Tester.resume()
                elif ( instructions.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    print("instruction menu")
                    Instructions.load()
            
menu()