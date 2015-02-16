'''
Created on Feb 13, 2015

@author: weismant
'''

import pygame
from Sprite import Sprite
from Boat import Boat

class FishingHook( Sprite ):
    
    '''
    * How fast the Eel moves per tick of the pygame clock. This quantity is
    * in pixels
    '''

    def __init__( self ):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/hook.png" ).convert() );
        pass
    
    '''
    * Draws this eel onto the screen 
    '''
    def draw( self , screen ):
        self.key_press()
        Sprite.draw( self , screen )
        pass
    
    def key_press(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
        if key[pygame.K_UP]: # right key
            if (self.y - dist <180):
                self.y = self.y
            else:   
                self.y -= dist # move right
        elif key[pygame.K_DOWN]: # left key
            if (self.y + dist >490):
                self.y = self.y
            else:   
                self.y += dist # move left

