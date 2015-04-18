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
import Customizations

from UIUtils import Button

pygame.init()
pygame.font.init()

background = pygame.image.load("res/MenuBackground.png")
backgroundRect = background.get_rect()


size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

instructionsBox = 0
        
def menu():
    continueGame = Button( (255,255,255) , "Buttons/ContinueButton.png" , (0 , 200) )
    newGame = Button((255,255,255), "Buttons/NewGameButton.png", (0, 250))
    instructions = Button((255,255,255), "Buttons/InstructionButton.png", (200, 200) )
    sentences = Button( (255,255,255) , "Buttons/SentencesButton.png" , (200 , 250) , (100,40) )
    customizations = Button( (255,255,255) , "Buttons/CustomizationsButton.png" , (400,200) )
    credits = Button ( (255,255,255) , "Buttons/creditsButton.png" , (400,250) )
    quit = Button( (255,255,255) , "Buttons/QuitButton.png" , (200,450) )
    
    jetpackMode = False
    jetpack = Button( (255,255,255), "res/testButton.png" , (450,450) , (50,50) )
    
    twoPlayerMode = False
    twoPlayer = Button( (255,255,255), "res/testButton.png" , (0,450) , (50,50) )
    
    Tester.restart()

    state = 0
    while state == 0:
        
        screen.fill([255,255,255])
        screen.blit(background, backgroundRect)
        screen.blit( continueGame.image , continueGame )
        screen.blit(newGame.image, newGame)
        screen.blit(instructions.image, instructions)
        screen.blit( sentences.image , sentences )
        screen.blit( customizations.image , customizations )
        screen.blit( credits.image , credits )
        screen.blit( jetpack.image , jetpack )
        screen.blit( twoPlayer.image , twoPlayer )
        screen.blit( quit.image , quit )
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit("quit game")
            if event.type == MOUSEBUTTONDOWN:
                loc = pygame.mouse.get_pos()
                if (continueGame.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    Tester.setBoatImage( Customizations.getSelectedBoat() )
                    Tester.resume()
                elif (newGame.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    Tester.setSentenceFile( SentenceSelector.getSelected() )
                    Tester.restart()
                    Tester.setBoatImage( Customizations.getSelectedBoat() )
                    Tester.resume()
                elif ( instructions.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    print("instruction menu")
                    Instructions.load()
                elif( sentences.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    SentenceSelector.load()
                    pass
                elif( customizations.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    Customizations.load()
                    pass
                elif( credits.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    Credits.load()
                    pass
                elif( jetpack.clicked(loc[ 0 ] , loc[ 1 ] ) ):
                    jetpackMode = not jetpackMode
                    print "Jetpack mode: " + str( jetpackMode )
                    Tester.setJetpackMode( jetpackMode )
                elif( twoPlayer.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    twoPlayerMode = not twoPlayerMode
                    print "Two player mode: " + str( twoPlayerMode )
                    Tester.setTwoPlayerMode( twoPlayerMode )
                elif ( quit.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    return
            
menu()