'''
Created on Apr 7, 2015

@author: mjchao
'''

import pygame 
from pygame.locals import *
import sys

from UIUtils import Button, Label
from SentenceListManager import SentenceListManager

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode( ( 500 , 500 ) )

sentenceManager = SentenceListManager()
selectedSentences = Label( (100,100) , (300,40) )
returnButton = Button( (255,255,255) , "Buttons/Return.png" , (0,0) )
prevButton = Button( (255,255,255) , "res/TriangleL.png" , (65,100) )
nextButton = Button( (255,255,255) , "res/TriangleR.png" , (400,100) )

instructionsLabel = Label( (50,40) , (500,60) )
instructionsLabel.setText( "Select a sentence file:" )
instructionsLabel.setBorderVisible( False )


def setSelectedSentences( sentenceFile ):
    selectedSentences.setText( sentenceFile )

def load():
    
    state = 1
    while( state != 0 ):
        screen.fill( [255 , 255 , 255] )
        screen.blit( returnButton.image , returnButton )
        screen.blit( prevButton.image , prevButton )
        screen.blit( nextButton.image , nextButton )
        
        screen.blit( instructionsLabel.image , instructionsLabel )
        selectedSentences.setText( sentenceManager.getSelectedFilename() )
        screen.blit( selectedSentences.image , selectedSentences )
        pygame.display.update()
        
        for event in pygame.event.get():
            if ( event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE ):
                return
            if ( event.type == MOUSEBUTTONDOWN ):
                loc = pygame.mouse.get_pos()
                if ( returnButton.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    return
                elif ( nextButton.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    sentenceManager.next()
                elif ( prevButton.clicked( loc[ 0 ] , loc[ 1 ] ) ):
                    sentenceManager.prev()
                    
                    
                