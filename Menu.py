'''
Created on Mar 3, 2015

@author: emkess
'''

import pygame 
from pygame.locals import *

import Tester
import Instructions
import sys


pygame.init()
pygame.font.init()

background = pygame.image.load("res/MenuBackground.png")
backgroundRect = background.get_rect()


size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

instructionsBox = 0


class Button(pygame.sprite.Sprite):
    def __init__(self, color, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (100,40))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
    
     
        
def menu():
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 40
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
                if (loc[0] > PLAY_BUTTON_LOCATION[0] and loc[0] < (PLAY_BUTTON_LOCATION[0] + BUTTON_WIDTH) and 
                    loc[1] > PLAY_BUTTON_LOCATION[1] and loc[1] < (PLAY_BUTTON_LOCATION[1] + BUTTON_HEIGHT)):
                    print("main game")
                    Tester.resume()
                elif (loc[0] > INSTRUCTION_BUTTON_LOCATION[0] and loc[0] < (INSTRUCTION_BUTTON_LOCATION[0] + BUTTON_WIDTH) and 
                      loc[1] > INSTRUCTION_BUTTON_LOCATION[1] and loc[1] < (INSTRUCTION_BUTTON_LOCATION[1] + BUTTON_HEIGHT)):
                    print("instruction menu")
                    Instructions.load()
            
menu()