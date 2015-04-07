'''
Created on Feb 13, 2015

@author: weismant
'''

import pygame
from Sprite import Sprite

class Boat( Sprite ):
    
    '''
    * How fast the Eel moves per tick of the pygame clock. This quantity is
    * in pixels
    '''

    def __init__( self):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        boatImage = pygame.image.load( "res/boat.png" ).convert()
        boatImage.set_colorkey( (255, 255, 255) )
        boatImage = pygame.transform.scale( boatImage , ( 180 , 140 ) )
        self.setImage( boatImage );
        pass
    
    '''
    * Draws this eel onto the screen 
    '''
    def draw( self , screen ):
        Sprite.draw( self , screen )

