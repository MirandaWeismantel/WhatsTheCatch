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
    
     
    def __init__( self , boat):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/line.png" ).convert() )
        self.setHeight(77)
        self.image = pygame.transform.scale(self.image, (5, self.height))
        self.boat = boat
        pass

        
    def moveTo( self , x , y ):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y-5
    
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
            if (self.height < 2):
                pass
            else:
                self.height -= 1   
                self.image = pygame.transform.scale(self.image, (5, self.height))
        elif key[pygame.K_DOWN]:
            if (self.y + dist >490):
                
                #don't let hook move too low, so we do nothing
                pass
            else:   
                self.height += 1
                #move left
                self.image = pygame.transform.scale(self.image, (5, self.height))
    

    '''
    * Handles collisions with other sprites
    '''
    def onCollide( self , otherSprite ):
        from Eel import Eel
        if ( isinstance( otherSprite , Eel ) ):
            self.remove()
                
    '''
    * Resets the fishing hook to start on the surface of the water again.
    * This is used when an eel hits the hook
    '''            
    def resetLine( self ):
        boatLocation = self.boat.getLocation()
        self.moveTo( boatLocation[ 0 ] , boatLocation[ 1 ] )
        

            