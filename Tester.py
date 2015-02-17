'''
Created on Feb 13, 2015

@author: mjchao, weismant

Testing module for graphics
'''


import pygame
from pygame.locals import *

from Eel import Eel
from Statistics import Statistics
from Fish import Fish
from Boat import Boat
from FishingHook import FishingHook
from Sentence import Word , Blank , Sentence

pygame.init()

background = pygame.image.load("res/background.png")
backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

#list of images to be drawn
images = []

#list of sprites to be drawn
sprites = []

#contains the player's score, lives, etc.
stats = Statistics()

#player starts with 3 lives
stats.addLife()
stats.addLife()
stats.addLife()

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

testFish = Fish()
testFish.moveTo(-50, 200)
sprites.append( testFish )

testBoat = Boat()
testBoat.moveTo(300, 100)
sprites.append( testBoat )

testHook = FishingHook()
testHook.moveTo(testBoat.x, 180)
sprites.append( testHook )

word1 = Word( "I" )
blank1 = Blank( [Word( "want" )] , [Word( "Ohio" ) , Word( "Yellow" ) ] )
word2 = Word( "a" )
blank2 = Blank( [Word("toy")] , [Word("eat") , Word( "run" ) , Word( "blue" )])
testSentence = Sentence( [word1 , blank1 , word2 , blank2 ] , "." )

filled = False
filled2 = False

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
        
        #check for collisions
        for i in range( 0 , len(sprites) ):
            for j in range( i+1 , len(sprites) ):
                sprite1 = sprites[ i ]
                sprite2 = sprites[ j ]
                if ( sprite1 != sprite2 ) :
                    if ( pygame.sprite.collide_rect( sprite1 , sprite2 ) ):
                        sprite1.onCollide( sprite2 )
                        sprite2.onCollide( sprite1 )
                    
        if testEel.x > 200 and not filled :
            testSentence.fillInNextBlank( Word( "want" ) )
            filled = True
            
        if testEel.x > 300 and not filled2 :
            testSentence.fillInNextBlank( Word( "toy" ) )
            filled2 = True
        testSentence.draw( screen )
        pygame.display.update()
    
    if ( stats.getLives() <= 0 ):
        state = 3
    
    #check if the user wants to quit
    for event in pygame.event.get():  
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 0
        if event.type == pygame.QUIT:
            state = 0
            
            
        