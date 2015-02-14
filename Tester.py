'''
Created on Feb 13, 2015

@author: mjchao

Testing module for graphics
'''


import pygame
from pygame.locals import *

from Eel import Eel

pygame.init()
screen = pygame.display.set_mode( [500 , 500] );

#list of images to be drawn
images = []

#list of sprites to be drawn
sprites = []

#just create all your images and sprites here and add them to the images
#and sprites list
testEel = Eel()
testEel.moveTo( 0 , 50 )
sprites.append( testEel )

testEel2 = Eel()
testEel2.EEL_SPEED = 0
testEel2.moveTo( 300 , 50 )
sprites.append( testEel2 )

#No need to modify the code below. It just runs the game.
state = 0
while( state == 0 ):
    
    #start with a new blank screen
    screen.fill( [255, 255, 255] )
    
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
                    
    
    pygame.display.update()
    
    #check if the user wants to quit
    for event in pygame.event.get():  
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 1
        if event.type == pygame.QUIT:
            state = 1
            
            
        