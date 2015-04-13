'''
Created on Mar 3, 2015

@author: emkess
'''

import pygame 
from pygame.locals import *

import Tester
import Instructions
import sys
import SentenceSelector
import Credits

from UIUtils import Button

pygame.init()
pygame.font.init()

background = pygame.image.load("res/MenuBackground.png")
backgroundRect = background.get_rect()


size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

instructionsBox = 0
        
def menu():
    MENU_BUTTON_SIZE = (100,40)
    continueGame = Button( (255,255,255) , "Buttons/ContinueButton.png" , (200 , 200) , MENU_BUTTON_SIZE )
    newGame = Button((255,255,255), "Buttons/NewGameButton.png", (200, 250) , MENU_BUTTON_SIZE )
    instructions = Button((255,255,255), "Buttons/InstructionButton.png", (200, 300) , MENU_BUTTON_SIZE )
    sentences = Button( (255,255,255) , "Buttons/SentencesButton.png" , (200 , 350) , MENU_BUTTON_SIZE )
    customizations = Button( (255,255,255) , "Buttons/CustomizationsButton.png" , (200,400) , MENU_BUTTON_SIZE )
    quitGame = Button( (255,255,255) , "Buttons/QuitButton.png" , (200,450) , MENU_BUTTON_SIZE )
    
    Tester.restart()
    Tester.setTwoPlayerMode( False )
    Tester.setJetpackMode( False )
    
    state = 0
    while state == 0:
        
        screen.fill([255,255,255])
        screen.blit(background, backgroundRect)
        screen.blit( continueGame.image , continueGame )
        screen.blit(newGame.image, newGame)
        screen.blit(instructions.image, instructions)
        screen.blit( sentences.image , sentences )
        screen.blit( customizations.image , customizations )
        screen.blit( quitGame.image , quitGame )
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit("quit game")
            if event.type == MOUSEBUTTONDOWN:
                print("mouse click")
                loc = pygame.mouse.get_pos()
                if (continueGame.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    Tester.resume()
                elif (newGame.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    print("main game")
                    Tester.setSentenceFile( SentenceSelector.getSelected() )
                    Tester.restart()
                    Tester.resume()
                elif ( instructions.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    print("instruction menu")
                    Instructions.load()
                elif( sentences.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    SentenceSelector.load()
                    pass
                elif( customizations.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    Credits.load()
                    pass
                elif ( quitGame.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    return
            
menu()