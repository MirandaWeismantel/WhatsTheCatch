'''
Created on Feb 13, 2015

@author: mjchao
'''

import pygame
from Sprite import Sprite
from FishingHook import FishingHook

class Eel( Sprite ):
    
    '''
    * How fast the Eel moves per tick of the pygame clock. This quantity is
    * in pixels
    '''
    EEL_SPEED = 1
    
    '''
    * The statistics object that stores the player's lives. The eel will
    * subtract lives from the statistics object if it touches the fishing line
    * or fishing hook
    '''
    stats = None
    
    def __init__( self , stats ):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/eel.png" ).convert() );
        self.stats = stats
    
    '''
    * Draws this eel onto the screen 
    '''
    def draw( self , screen ):
        Sprite.draw( self , screen )
        pass
    
    '''
    * Moves the eel to the right by the speed of an eel
    '''
    def animate( self ):
        self.move( self.EEL_SPEED , 0 );
        
    '''
    * Handles what happens when collision is detected
    '''
    def onCollide( self , otherSprite ):
        if ( isinstance( otherSprite , FishingHook ) ):
            self.stats.subtractLife()
            pass