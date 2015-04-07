'''
Created on Feb 13, 2015

@author: weismant
'''

import pygame
from Sprite import Sprite
from Boat import Boat

class FishingLine( Sprite ):

    
    '''
    * The boat to which this fishing line belongs
    '''
    boat = None
    
    twoPlayerMode = False
     
    def __init__( self , boat):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/line.png" ).convert() )
        self.setHeight(77)
        self.image = pygame.transform.scale(self.image, (5, self.height))
        self.boat = boat
        pass
    
    '''
    * Draws this fishing hook onto the screen 
    '''
    def draw( self , screen ):
        self.key_press()
        Sprite.draw( self , screen )
        pass
    
    def key_press(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1
        
        if ( self.twoPlayerMode ):
            rightKeyPressed = key[ pygame.K_d ]
            leftKeyPressed = key[ pygame.K_a ]
        else :
            rightKeyPressed = key[ pygame.K_RIGHT ]
            leftKeyPressed = key[ pygame.K_LEFT ]
            
        if rightKeyPressed and ( self.boat.x + dist <= 450 ): # right key
            
            #move fishing hook right
            self.move( dist , 0 )
        elif leftKeyPressed and (self.boat.x - dist >= 0 ): # left key
            
            #move fishing hook left
            self.move( -1*dist , 0 )
        if key[pygame.K_UP]:
            if (self.height < 20):
                pass
            else: 
                self.image = pygame.transform.scale(self.image, (5, self.height))
                self.setHeight( self.getHeight()-1 )
        elif key[pygame.K_DOWN]:
            if (self.y + self.getHeight() + dist >500):
                
                #don't let hook move too low, so we do nothing
                pass
            else:   
                #move left
                self.image = pygame.transform.scale(self.image, (5, self.height))
                self.setHeight( self.getHeight()+1 )
    

    '''
    * Handles collisions with other sprites
    '''
    def onCollide( self , otherSprite ):
        from Eel import Eel
        if ( isinstance( otherSprite , Eel ) ):
            pass
                
    '''
    * Resets the fishing hook to start on the surface of the water again.
    * This is used when an eel hits the hook
    '''            
    def resetLine( self ):
        boatLocation = self.boat.getLocation()
        self.setHeight( 1 )
        self.image = pygame.transform.scale(self.image, (5, self.height))
        self.moveTo( boatLocation[ 0 ]+31 , 122 )
    

            