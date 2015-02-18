'''
Created on Feb 13, 2015

@author: mjchao, weismant

Testing module for graphics
'''


import pygame, random
import random
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

#list of sentences to be used
sentences = []

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
sentence1 = Sentence( [word1 , blank1 , word2 , blank2 ] , "." )

s2word1 = Word( "A cute" )
s2blank1 = Blank( [Word( "kitten" ), Word("puppy")] , [Word( "cactus" ) , Word( "jump" ) ] )
s2word2 = Word( "is a" )
s2blank2 = Blank( [Word("pet")] , [Word("toy") , Word( "food" ) , Word( "orange" )])
sentence2 = Sentence( [s2word1 , s2blank1 , s2word2 , s2blank2 ] , "." )
sentences.append(sentence2)

s3word1 = Word( "Let's go to the" )
s3blank1 = Blank( [Word( "store" )] , [Word( "ear" ) , Word( "long" ) ] )
s3word2 = Word( "to" )
s3blank2 = Blank( [Word("buy"), Word("get")] , [Word("wake") , Word( "flower" ) , Word( "orange" )])
s3word3 = Word( "some" )
s3blank3 = Blank( [Word("bread"), Word("milk")] , [Word("hair") , Word( "canyon" )])
sentence3 = Sentence( [s3word1 , s3blank1 , s3word2 , s3blank2, s3word3, s3blank3 ] , "." )
sentences.append(sentence3)

s4word1 = Word( "I like to" )
s4blank1 = Blank( [Word( "give" )] , [Word( "oil" ) , Word( "shirt" ) ] )
s4word2 = Word( "my friends" )
s4blank2 = Blank( [Word("hugs"), Word("toys")] , [Word( "9" ) , Word( "rain" )])
sentence4 = Sentence( [s4word1 , s4blank1 , s4word2 , s4blank2 ] , "." )
sentences.append(sentence4)

s5word1 = Word( "The snow is" )
s5blank1 = Blank( [Word( "white" )] , [Word( "ill" ) , Word( "goat" ) ] )
s5word2 = Word( "and" )
s5blank2 = Blank( [Word("cold")] , [Word( "far" ) , Word( "up" )])
sentence5 = Sentence( [s5word1 , s5blank1 , s5word2 , s5blank2 ] , "." )
sentences.append(sentence5)

endWord = Word( "Congratulations!!" )
endSentence = Sentence( [endWord] , "." )


#CONTINUE HERE
#create a random word that will be passed and drawn on the fish
#first create a random number that will stand for either a word from the incorrect or correct list
#correctOrIncorrectList = random.randrange(1,2,1)
#create a random number that will select a word from the appropriate list
#if (correctOrIncorrectList == 1):
    #wordNum = random.randrange(1,blank1)
testSentence = sentence1
    
def createFish( word ):
    newFish = Fish( word )
    newFish.moveTo( random.randrange( -500 , 0 ) , random.randrange( 200 , 450 ) )
    print "Fish moved to " + str( newFish.x ) + " " + str( newFish.y )
    sprites.append( newFish )
    fishes.append( newFish )
    
totalAcceptableFish = 3
totalUnacceptableFish = 2

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
    for fish in fishes:
        sprites.remove( fish )
    del fishes[:]
    testSentence.deleteWords() 
    testSentence = random.choice(sentences)
    sentences.remove(testSentence)
    '''
    word1 = Word( "I" )
    blank1 = Blank( [Word( "want" )] , [Word( "Ohio" ) , Word( "Yellow" ) ] )
    word2 = Word( "a" )
    blank2 = Blank( [Word("toy")] , [Word("eat") , Word( "run" ) , Word( "blue" )])
    testSentence = Sentence( [word1 , blank1 , word2 , blank2 ] , "." )
    '''

#just create all your images and sprites here and add them to the images
#and sprites list
testEel = Eel( stats )
testEel.EEL_SPEED = 1.5      #in the future this can be randomized
testEel.moveTo( -250 , 300 )
sprites.append( testEel )

testEel2 = Eel( stats )
testEel2.EEL_SPEED = 2
testEel2.moveTo( -100 , 300 )
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
# 3 = game is over (i.e. player has to start a new game

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
                        if not sentences:
                            testSentence = endSentence;
                        if sentences:    
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
            
            
        