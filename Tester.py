'''
Created on Feb 13, 2015

@author: mjchao, weismant

Testing module for graphics
'''


import pygame, random
from pygame.locals import *

from Eel import Eel
from Statistics import Statistics
from Fish import Fish
from Boat import Boat
from FishingHook import FishingHook
from Sentence import Word , Blank , Sentence

pygame.init()
pygame.font.init()

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

#contains the player's score, lives, etc.
stats = Statistics()
statsFont = pygame.font.SysFont('Courier New', 15)
def drawStats( screen ):
    global stats
    global statsFont
    livesText = "Lives: " + str( stats.getLives() )
    text = statsFont.render(livesText , True , (0, 0, 0))
    screen.blit( text , (400 , 0 ) )
    

#player starts with 3 lives
stats.addLife()
stats.addLife()
stats.addLife()

word1 = Word( "I" )
blank1 = Blank( [Word( "want" )] , [Word( "Ohio" ) , Word( "Yellow" ) ] )
word2 = Word( "a" )
blank2 = Blank( [Word("toy")] , [Word("eat") , Word( "run" ) , Word( "blue" )])
testSentence = Sentence( [word1 , blank1 , word2 , blank2 ] , "." )


#CONTINUE HERE
#create a random word that will be passed and drawn on the fish
#first create a random number that will stand for either a word from the incorrect or correct list
#correctOrIncorrectList = random.randrange(1,2,1)
#create a random number that will select a word from the appropriate list
#if (correctOrIncorrectList == 1):
    #wordNum = random.randrange(1,blank1)
    
def createFish( word ):
    newFish = Fish( word )
    newFish.moveTo( -50 , random.randrange( 200 , 300 ) )
    sprites.append( newFish )
    fishes.append( newFish )
    
totalAcceptableFish = 1
totalUnacceptableFish = 1
def generateFish():
    global totalAcceptableFish
    global totalUnacceptableFish
    
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
        

#TODO
def createNewSentence():
    global testSentence
    word1 = Word( "I" )
    blank1 = Blank( [Word( "want" )] , [Word( "Ohio" ) , Word( "Yellow" ) ] )
    word2 = Word( "a" )
    blank2 = Blank( [Word("toy")] , [Word("eat") , Word( "run" ) , Word( "blue" )])
    testSentence = Sentence( [word1 , blank1 , word2 , blank2 ] , "." )

#just create all your images and sprites here and add them to the images
#and sprites list
testEel = Eel( stats )
testEel.EEL_SPEED = 0
testEel.moveTo( 0 , 300 )
sprites.append( testEel )

testEel2 = Eel( stats )
testEel2.EEL_SPEED = 0
testEel2.moveTo( 300 , 300 )
sprites.append( testEel2 )

testFish = Fish( Word( "want" ) )
testFish.moveTo(-50, 200)
sprites.append( testFish )
fishes.append( testFish )

testBoat = Boat()
testBoat.moveTo(300, 100)
sprites.append( testBoat )

testHook = FishingHook( testBoat )
testHook.moveTo(testBoat.x, 180)
sprites.append( testHook )

#No need to modify the code below. It just runs the game.

# States:
# 0 = terminate program
# 1 = game is running
# 2 = game is paused
# 3 = game is over (i.e. player has to start a new game)
state = 1
while( state != 0 ):
    
    if ( state == 1 ):
        #start with the background image and get the user input from the boat
        screen.blit(background, backgroundRect)
        
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
                        testSentence.fillInNextBlank( fish.word )
                        fishes.remove( fish )
                        sprites.remove( fish )
                        generateFish()
                        testHook.resetHook()
                    
                    if ( testSentence.isComplete() ):
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
                    
        testSentence.draw( screen )
        drawStats( screen )
        
        pygame.display.update()
    
    if ( stats.getLives() <= 0 ):
        state = 3
    
    #check if the user wants to quit
    for event in pygame.event.get():  
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 0
        if event.type == pygame.QUIT:
            state = 0
            
            
        