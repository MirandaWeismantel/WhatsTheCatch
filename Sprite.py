'''
Created on Feb 12, 2015

@author: mjchao
'''

import pygame
from pygame.locals import *

from Image import Image

'''
* Represents a Sprite, which is a graphical element capable of 
* changing in appearance (animation), and is capable of moving around 
* the screen. This interface provides methods for moving and drawing
* the Sprite. Examples of Sprites would include Fish, Eel, and FishingLine
'''
class Sprite( Image ):
    
    '''
    * Draws this sprite onto the screen in the appropriate location and with
    * the appropriate graphical appearance. This should be overridden
    * in subclasses.
    '''
    def draw( self ):
        pass
    
    '''
    * Moves the animation of this sprite forward by 1 frame, 
    * if this sprite can be animated. The frame rate is not handled by this
    * method. This method does not have to do anything if the sprite is
    * not animated.
    '''
    def animate( self ):
        pass
    
    '''
    * Sets the sprite's location to the given coordinates
    *
    * @param x         the new x coordinates for the sprite, in pixels
    * @param y         the new y coordinates for the sprite, in pixels
    '''
    def moveTo( self , x , y ):
        self.x = x
        self.y = y
    
    '''
    * Moves the sprite by the given amounts in the x and y directions
    *
    * @param dx         amount by which to move in the x direction, in pixels
    * @param dy         amount by which to move in the y direction , in pixels
    '''
    def move( self , dx , dy ):
        self.x += dx
        self.y += dy
    
    '''
    * Handles what happens when this sprite collides with another sprite. 
    * This method should not be called directly except by the GameWindow, which
    * will handle collisions at a higher level.
    *
    * @param otherSprite     the sprite with which this sprite collided
    '''
    def onCollide( self , otherSprite ):
        pass