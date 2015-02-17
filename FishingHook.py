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
    
    '''
    * The fish that is currently hooked (None, if no fish is hooked)
    '''
    hookedFish = None
     
    def __init__( self , boat ):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/hook.png" ).convert() );
        self.boat = boat
        self.setHeight( 40 )
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
    * @param          a fish that might possibly be hooked by this fishing hook
    * @return         if the fishing hook can hook another fish. Only one fish
    *                 can be on a fishing hook at any time
    '''
    def canHookFish( self , fish ):
        
        #if we don't have a fish on the hook right now, then we can hook
        #this provided fish
        if self.hookedFish == None:
            return True
        
        #if the provided fish is the fish that is currently hooked, then
        #of course we can hook it. This is necessary depending on whether
        #fish.onCollide( fishingHook ) happened first or whether
        #fishingHook.onCollide( fish ) happened first. If fishingHook's
        #onCollide happened first, then its hookedFish is already updated
        #thus, when the fish calls canHookFish(...) on the fishing hook,
        #self.hookedFish of the fishing hook has already been updated.
        #thus, we cannot just check self.hookFish == None
        else:
            return self.hookedFish == fish
    
    '''
    * Handles collisions with other sprites
    '''
    def onCollide( self , otherSprite ):
        from Fish import Fish
        if ( isinstance( otherSprite , Fish ) ):
            if ( self.hookedFish == None ):
                self.hookedFish = otherSprite
                
    '''
    * Resets the fishing hook to start on the surface of the water again.
    * This is used when an eel hits the hook
    '''            
    def resetHook( self ):
        boatLocation = self.boat.getLocation()
        self.moveTo( boatLocation[ 0 ] , boatLocation[ 1 ] )
        if ( not self.hookedFish == None ):
            self.hookedFish.unhook()
            self.hookedFish = None
            

