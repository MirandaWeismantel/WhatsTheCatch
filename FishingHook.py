'''
Created on Feb 13, 2015

@author: weismant
'''

import pygame
from Sprite import Sprite
from Boat import Boat
from FishingLine import FishingLine

class FishingHook( Sprite ):

    
    '''
    * The boat to which this fishing hook belongs
    '''
    boat = None
    
    '''
    * The fish that is currently hooked (None, if no fish is hooked)
    '''
    hookedFish = None
    
    '''
    * If we are in two player mode or not (in two player mode, the controls
    * change where A,D moves the boat left and right and UP/DOWN moves the
    * hook up and down
    '''
    twoPlayerMode = False
    
    moveRate = 1
     
    def __init__( self , boat, line):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        hookImage = pygame.image.load( "res/hook.png" );
        hookImage = pygame.transform.scale( hookImage , ( 50 , 50 ) );
        self.setImage( hookImage );
        self.boat = boat
        self.line = line
        self.setHeight( 35 )
        self.setWidth( 30 )
        pass
    
    def moveTo( self , x , y ):
        self.x = x
        self.y = y
        self.rect.x = x+5
        self.rect.y = y
    
    def moveHookedFish( self , dx , dy ):
        if ( self.hookedFish != None ):
            self.hookedFish.moveTo( self.hookedFish.x + dx , self.hookedFish.y + dy )
    
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
        
        if ( self.twoPlayerMode ):
            rightKeyPressed = key[ pygame.K_d ]
            leftKeyPressed = key[ pygame.K_a ]
        else :
            rightKeyPressed = key[ pygame.K_RIGHT ]
            leftKeyPressed = key[ pygame.K_LEFT ]
            
        if rightKeyPressed and (self.boat.x + self.moveRate <= 450) : # right key
            
            #move fishing hook right
            self.move( self.moveRate , 0 )
            self.moveHookedFish( self.moveRate , 0 )
            self.boat.move( self.moveRate , 0 )
        elif leftKeyPressed and (self.boat.x - self.moveRate >= 0) : # left key
            
            #move fishing hook left
            self.move( -1*self.moveRate , 0 )
            self.moveHookedFish( -1*self.moveRate , 0 )
            self.boat.move( -1*self.moveRate , 0 )
        if key[pygame.K_UP]:
            self.moveHookedFish( 0 , -1*self.moveRate )
            if (self.y - self.moveRate <105):
                
                #don't let hook move too high, so we do nothing
                pass
            else:   
                
                #move right
                self.move( 0 , -1*self.moveRate )
        elif key[pygame.K_DOWN]:
            if (self.y + self.moveRate >490):
                
                #don't let hook move too low, so we do nothing
                pass
            else:   
                
                #move left
                self.move( 0 , self.moveRate )
                self.moveHookedFish( 0 , self.moveRate )
        if key[pygame.K_SPACE]:
            self.hookedFish = None

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
        self.moveTo( boatLocation[ 0 ] , 115 )
        self.line.setHeight(10)
        self.line.image = pygame.transform.scale(self.line.image, (5, self.height))
        if ( not self.hookedFish == None ):
            self.hookedFish.unhook()
            self.hookedFish = None
            
            

