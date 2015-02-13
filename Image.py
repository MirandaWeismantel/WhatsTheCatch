'''
Created on Feb 12, 2015

@author: mjchao

A general interface that represents an image to be drawn on the screen.
It is unchanging
'''

import pygame
from pygame.locals import *

class Image( pygame.sprite.Sprite ):
    
    '''
    Draws the image onto the screen. It must be implemented in subclasses
    '''
    def draw(self):
        pass
        
    