'''
Created on Apr 7, 2015

@author: mjchao
'''

import pygame 
from pygame.locals import *
import sys

from UIUtils import Button, Label
from SentenceListManager import SentenceListManager
import ScoreManager

pygame.init()
pygame.font.init()

MASTERY_X = 50
MASTERY_Y = 100
MASTERY_WIDTH = 500
MASTERY_HEIGHT = 40

INSTRUCTIONS_X = 50
INSTRUCTIONS_Y = MASTERY_Y + MASTERY_HEIGHT
INSTRUCTIONS_WIDTH = 500
INSTRUCTIONS_HEIGHT = 40

SELECT_X = INSTRUCTIONS_X + 50
SELECT_Y = INSTRUCTIONS_Y + INSTRUCTIONS_HEIGHT
SELECT_WIDTH = 300
SELECT_HEIGHT = 40
PREV_BTN_X = SELECT_X - 35
PREV_BTN_Y = SELECT_Y
NEXT_BTN_X = SELECT_X + SELECT_WIDTH
NEXT_BTN_Y = SELECT_Y

BEST_STATS_X = 50
BEST_STATS_Y = SELECT_Y + SELECT_HEIGHT
BEST_STATS_WIDTH = 500
BEST_STATS_HEIGHT = 40


screen = pygame.display.set_mode( ( 500 , 500 ) )

sentenceManager = SentenceListManager()
selectedSentences = Label( ( SELECT_X ,SELECT_Y ) , ( SELECT_WIDTH ,SELECT_HEIGHT ) )
returnButton = Button( (255,255,255) , "Buttons/Return.png" , (0,0) )
prevButton = Button( (255,255,255) , "res/TriangleL.png" , ( PREV_BTN_X , PREV_BTN_Y ) )
nextButton = Button( (255,255,255) , "res/TriangleR.png" , (NEXT_BTN_X , NEXT_BTN_Y ) )

masteryLabel = Label( ( MASTERY_X , MASTERY_Y ) , ( MASTERY_WIDTH , MASTERY_HEIGHT ) )
masteryLabel.setText( "0/0 sentence sets mastered!" )
masteryLabel.setBorderVisible( False )

instructionsLabel = Label( ( INSTRUCTIONS_X , INSTRUCTIONS_Y ) , ( INSTRUCTIONS_WIDTH , INSTRUCTIONS_HEIGHT ) )
instructionsLabel.setText( "Select a sentence file:" )
instructionsLabel.setBorderVisible( False )

bestStatsLabel = Label( ( BEST_STATS_X , BEST_STATS_Y ) , ( BEST_STATS_WIDTH , BEST_STATS_HEIGHT ) )
bestStatsLabel.setText( "Best score: 0/0" )
bestStatsLabel.setBorderVisible( False )


def setSelectedSentences( sentenceFile ):
    selectedSentences.setText( sentenceFile )

def load():
    ScoreManager.initialize()
    masteryLabel.setText( str(ScoreManager.getNumSetsMastered()) + "/" + 
            str(ScoreManager.getTotalSets()) + " sentence sets mastered!" ) 
    state = 1
    while( state != 0 ):
        screen.fill( [255 , 255 , 255] )
        screen.blit( returnButton.image , returnButton )
        screen.blit( prevButton.image , prevButton )
        screen.blit( nextButton.image , nextButton )
        
        screen.blit( masteryLabel.image , masteryLabel )
        screen.blit( instructionsLabel.image , instructionsLabel )
        
        selectedSentences.setText( sentenceManager.getSelectedFilename() )
        screen.blit( selectedSentences.image , selectedSentences )
        
        statsText = ("Best score: " +
            ": " + str(ScoreManager.getScoreFor( sentenceManager.getSelectedFilename() )) + 
            "/" + str(ScoreManager.getMaxPointsFor(sentenceManager.getSelectedFilename() ) ))
        bestStatsLabel.setText( statsText )
        screen.blit( bestStatsLabel.image , bestStatsLabel )
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
                    
def getSelected():
    return sentenceManager.getSelectedFilename()
                    
                    
                