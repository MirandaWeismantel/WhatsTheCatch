'''
Created on Feb 13, 2015

@author: weismant
'''

import pygame
from Sprite import Sprite
from Boat import Boat

class FishingHook( Sprite ):

    
    '''
    * The boat to which this fishing hook belongs
    '''
    boat = None
     
    def __init__( self , boat ):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/hook.png" ).convert() );
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
        if key[pygame.K_RIGHT]: # right key
            
            #move fishing hook right
            self.move( dist , 0 )
        elif key[pygame.K_LEFT]: # left key
            
            #move fishing hook left
            self.move( -1*dist , 0 )
        if key[pygame.K_UP]:
            if (self.y - dist <100):
                
                #don't let hook move too high, so we do nothing
                pass
            else:   
                
                #move right
                self.move( 0 , -1*dist )
        elif key[pygame.K_DOWN]:
            if (self.y + dist >490):
                
                #don't let hook move too low, so we do nothing
                pass
            else:   
                
                #move left
                self.move( 0 , dist )
    
    '''
    * Resets the fishing hook to start on the surface of the water again.
    * This is used when an eel hits the hook
    '''            
    def resetHook( self ):
        boatLocation = self.boat.getLocation()
        self.moveTo( boatLocation[ 0 ] , boatLocation[ 1 ] )
            

