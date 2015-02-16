'''
    Created on Feb 13, 2015
    
    @author: weismant
    '''

import pygame
from Sprite import Sprite
from Eel import Eel

class Fish( Sprite ):
    
    '''
        * How fast the Eel moves per tick of the pygame clock. This quantity is
        * in pixels
        '''
    fishSpeed = 1
    fishShift = 50
    
    def __init__( self ):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/fish.png" ).convert() );
        pass
    
    '''
        * Draws this eel onto the screen
        '''
    def draw( self , screen ):
        Sprite.draw( self , screen )
        pass
    
    '''
        * Draws this eel onto the screen
        '''
    def move(self, dx, dy):
        if (self.x + dx == 600):
            self.fishSpeed = -1
            self.moveTo( self.x , self.y + dy )
            self.flipImage()
        elif (self.x + dx == -100):
            self.fishSpeed = 1
            self.moveTo( self.x , self.y + dy )
            self.flipImage()
        if (self.y + dy < 160):
            self.fishShift = 50
        elif (self.y + dy > 500):
            self.fishShift = -50
        self.moveTo( self.x + dx , self.y )
        
    
    '''
        * Moves the eel to the right by the speed of an eel
        '''
    def animate( self ):
        self.move( self.fishSpeed , self.fishShift );
    
    '''
        * Handles what happens when collision is detected
        '''
    def onCollide( self , otherSprite ):
        if ( isinstance( otherSprite , Eel ) ):
            print "Collision detected!"
            
    def flipImage(self):
        self.image = pygame.transform.flip(self.image, 1, 0)
