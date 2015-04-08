'''
ATTENTION: If you're grading this, please read README.md first
To start, run the program in Eclipse
To restart, exit and start again
When you're done, please exit the game
'''

'''
Created on Feb 13, 2015

@author: mjchao, weismant

Testing module for graphics
'''


import pygame
import random
from pygame.locals import *

from Eel import Eel
from Statistics import Statistics
from Fish import Fish
from Boat import Boat
from FishingHook import FishingHook
from Sentence import Word , Sentence
from FishingLine import FishingLine
from SentenceFactory import SentenceFactory
from UIUtils import Button
import ScoreManager

pygame.init()
pygame.font.init()
ScoreManager.initialize()

background = pygame.image.load("res/background.png")
backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

#list of images to be drawn
images = []

#list of sprites to be drawn
sprites = []

#list of active fish in the ocean
fishes = []

#list of active eels on the screen
eels = []

#contains the player's score, lives, etc.
stats = Statistics()
statsFont = pygame.font.SysFont('Courier New', 15)

fishSpeed = 1;
eelSpeed = 1.5;

def drawStats( screen ):
    global stats
    global statsFont
    livesText = "Lives: " + str( stats.getLives() )
    text = statsFont.render(livesText , True , (0, 0, 0))
    screen.blit( text , (400 , 0 ) )
    
    scoreText = "Score: " + str( stats.getPoints() );
    text = statsFont.render( scoreText , True , (0, 0, 0))
    screen.blit( text , (400 , 20 ) )
    

#player starts with 3 lives
def resetStats():
    global stats
    stats = Statistics();
    stats.addLife()
    stats.addLife()
    stats.addLife()

factory = None
sentenceSet = " A"
sentenceFilename = "sentences/ A"
def resetSentenceFactory():
    global factory
    factory = SentenceFactory( sentenceFilename )

    #check that the data file is formatted correctly
    factory.validate()

testSentence = None
    
endWord = Word( "Congratulations!!" )
endSentence = Sentence( [endWord] , "!" )  

lostWord = Word( "You are out of lives!!" )
lostSentence = Sentence( [lostWord] , "!" )  
    
def createFish( word ):
    global fishes
    global sprites
    newFish = Fish( word, fishSpeed )
    newFish.moveTo( random.randrange( -500 , 0 ) , random.randrange( 200 , 420 ) )
    sprites.append( newFish )
    fishes.append( newFish )
    changeSpeed()
    
def changeSpeed( ):
    numCompletedSentences = stats.getCompletedSentenceCount()
    if numCompletedSentences > 10:
        eelSpeed = 3
        fishSpeed = 2.5
        for eel in eels:
            eel.updateSpeed(3)
        for fish in fishes:
            fish.updateSpeed(2.5)
    elif numCompletedSentences > 5:
        eelSpeed = 2.5
        fishSpeed = 2
        for eel in eels:
            eel.updateSpeed(2.5)
        for fish in fishes:
            fish.updateSpeed(2)
    else: 
        eelSpeed = 1.5
        fishSpeed = 1
        for eel in eels:
            eel.updateSpeed(1.5)
        for fish in fishes:
            fish.updateSpeed(1)
    
totalAcceptableFish = 3
totalUnacceptableFish = 2

def generateFish():
    global totalAcceptableFish
    global totalUnacceptableFish
    global fishes
    global sprites
    
    for fish in fishes:
        sprites.remove( fish )
        
    fishes = []
    
    if testSentence.isComplete():
        return
    
    numAcceptableFish = 0
    acceptableWords = testSentence.getAcceptableWordsForNextBlank()
    
    numUnacceptableFish = 0
    unacceptableWords = testSentence.getUnacceptableWordsForNextBlank()
    for fish in fishes:
        for word in testSentence.getAcceptableWordsForNextBlank():
            if fish.word.equals( word ):
                numAcceptableFish += 1
                break
        for word in testSentence.getUnacceptableWordsForNextBlank():
            if fish.word.equals( word ):
                numUnacceptableFish += 1
    
    while numAcceptableFish < totalAcceptableFish:
        createFish( acceptableWords[ random.randrange( 0 , len( acceptableWords ) ) ] )
        numAcceptableFish += 1
    
    while numUnacceptableFish < totalUnacceptableFish:
        createFish( unacceptableWords[ random.randrange( 0 , len( unacceptableWords ) ) ] )
        numUnacceptableFish += 1
    
def createNewSentence():
    global testSentence
    global fishes
    global sprites
    global factory
    global endSentence
    global stats
    
    for fish in fishes:
        sprites.remove( fish )
    del fishes[:]
    fishes = []
    
    if ( factory.hasMoreSentences() ):
        testSentence = factory.next()
    else :
        testSentence = endSentence
        ScoreManager.updateScore( sentenceSet , stats.getPoints() , factory.getMaxPoints() )
        ScoreManager.saveScores()
        for eel in eels:
            sprites.remove( eel )
        del eels[:]
        
testHook = None
testBoat = None
testLine = None

'''
* Resets everything - the fish, the score, etc.
'''
def restart():
    global sprites, images, fishes, eels , state , testHook , testBoat , testLine
    state = 0
    sprites = []
    images = []
    fishes = []
    eels = []
    
    resetSentenceFactory()
    resetStats()
    
    #just create all your images and sprites here and add them to the images
    #and sprites list
    
    testBoat = Boat()
    testBoat.moveTo(300, 50)
    sprites.append( testBoat )
    changeSpeed()
    
    testLine = FishingLine(testBoat)
    testLine.moveTo(testBoat.x + 31, 122)
    sprites.append( testLine )
    
    testHook = FishingHook( testBoat, testLine )
    testHook.moveTo(testBoat.x, 180)
    sprites.append( testHook )
    
    testEel = Eel( stats , testHook , testLine, eelSpeed )
    testEel.EEL_SPEED = 1.5      #in the future this can be randomized
    testEel.moveTo( -250 , 250 )
    eels.append( testEel )
    sprites.append( testEel )
    
    testEel2 = Eel( stats , testHook , testLine, eelSpeed )
    testEel2.EEL_SPEED = 2
    testEel2.moveTo( -100 , 400 )
    eels.append( testEel2 )
    sprites.append( testEel2 )
    
    createNewSentence()
    generateFish()

def createEel():
    newEel = Eel( stats , testHook , testLine, eelSpeed )
    newEel.moveTo( -250, 300 ) #TODO Make Random
    sprites.append( newEel )
    eels.append( newEel )
    changeSpeed()
    #testEel.EEL_SPEED = 1.5 #TODO Make random (negative and positive)


#No need to modify the code below. It just runs the game.

# States:
# 0 = terminate program
# 1 = game is running
# 2 = game is paused
# 3 = game is over (i.e. player has to start a new game

state = 0

'''
* Runs the game
'''
def mainGame():
    
    
    global state , testSentence , lostSentence
    state = 1
    backToMenu = Button((255,255,255), "Buttons/Return.png", (0,0))
    while( state != 0 ):

        if ( state == 1 ):
            #start with the background image and get the user input from the boat
            screen.blit(background, backgroundRect)

            screen.blit( backToMenu.image , backToMenu )
            
            #draw images into the background
            for image in images:
                image.draw( screen )
                
            #draw sprites on top of the images
            for sprite in sprites:
                sprite.animate()
                sprite.draw( screen )
                        
            for fish in fishes:
                if ( isinstance( fish , Fish ) ):
                    if ( fish.caught ):
                        if ( not testSentence.isComplete() ):
                            success = testSentence.fillInNextBlank( fish.word )
                            if ( success ):
                                stats.addPoints( SentenceFactory.POINTS_PER_CORRECT_WORD );
                                generateFish()
                            else:
                                stats.subtractPoints( SentenceFactory.POINTS_PER_INCORRECT_WORD );
                                fishes.remove( fish )
                                sprites.remove( fish )
                            #fishes.remove( fish )
                            #sprites.remove( fish )
                            #generateFish()
                            testHook.resetHook()
                        
                        if ( testSentence.isComplete() ): 
                                stats.addPoints( SentenceFactory.POINTS_PER_SENTENCE )
                                stats.incrementCompletedSentences() 
                                createNewSentence()
                                generateFish()
            
            #check for collisions
            for i in range( 0 , len(sprites) ):
                for j in range( i+1 , len(sprites) ):
                    sprite1 = sprites[ i ]
                    sprite2 = sprites[ j ]
                    if ( sprite1 != sprite2 ) :
                        if ( pygame.sprite.collide_rect( sprite1 , sprite2 ) ):
                            sprite1.onCollide( sprite2 )
                            sprite2.onCollide( sprite1 )
                            
            if ( stats.getLives() <= 0 ):
                testSentence = lostSentence
            
            testSentence.draw( screen )
            drawStats( screen )
            
            pygame.display.update()
            
        elif state == 3:
            pass
        
        if ( stats.getLives() <= 0 ):
            state = 3
        
        #check if the user wants to quit
        for event in pygame.event.get():  
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                state = 0
            if event.type == pygame.QUIT:
                state = 0               
            if ( event.type == MOUSEBUTTONDOWN ):
                loc = pygame.mouse.get_pos()
                if backToMenu.clicked( loc[ 0 ] , loc[ 1 ] ) :
                    if ( state == 3 ):
                        restart()
                    pause()
                    return
        

'''
* Pauses the game and hides the game window
'''
                
def pause():
    global state
    state = 0
    
'''
* Resumes the game and shows the game window
'''
def resume():
    global state
    state = 1
    mainGame()
    
def getState():
    global state
    return state

def setSentenceFile( filename ):
    global sentenceFilename , sentenceSet
    sentenceSet = filename
    sentenceFilename = "sentences/" + filename
    
def setTwoPlayerMode( on ):
    global testHook
    if ( on ):
        testHook.twoPlayerMode = True
        testLine.twoPlayerMode = True
    else:
        testHook.twoPlayerMode = False
        testLine.twoPlayerMode = False
          
#mainGame()
