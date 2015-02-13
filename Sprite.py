'''
Created on Feb 12, 2015

@author: mjchao
'''

import pygame
from pygame.locals import *

from Image import Image

class Sprite( Image ):
    
    x = 0
    y = 0
    width = 0
    height = 0
    
    '''
    
    '''
    def draw(self):
        pass
    
    '''
    Moves the animation of this sprite forward by 1 frame, 
    if this sprite can be animated. The frame rate is not handled by this
    method.
    '''
    def animate(self):
        pass
    
    '''
    
    '''
    def moveTo( self , x , y ):
        self.x = x
        self.y = y
    
    def getLocation(self):
        return [self.x, self.y]
    
    def move( self , dx , dy ):
        self.x += dx
        self.y += dy
    
    def onCollide( self , otherSprite ):
        pass
    
    def setWidth( self , width ):
        self.width = width
        
    def setHeight( self , height ):
        self.height = height
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height