'''
Created on Feb 13, 2015

@author: mjchao
'''

import pygame
from Sprite import Sprite
from FishingHook import FishingHook
from FishingLine import FishingLine

pygame.mixer.init()
# ShockSound = pygame.mixer.Sound('res/ShockSound.wav')

class Eel( Sprite ):
    
    '''
    * How fast the Eel moves per tick of the pygame clock. This quantity is
    * in pixels
    '''
    EEL_SPEED = 1
    EEL_SHIFT = 30
    speed = 1
    
    '''
    * The statistics object that stores the player's lives. The eel will
    * subtract lives from the statistics object if it touches the fishing line
    * or fishing hook
    '''
    stats = None
    
    fishingHook = None
    fishingLine = None
    
    def __init__( self , stats , fishingHook , fishingLine, eelSpeed ):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/eel.png" ).convert() );
        self.stats = stats
        
        self.fishingHook = fishingHook
        self.fishingLine = fishingLine
        
        #slightly offset eel picture's extra whitespace width
        self.setWidth( 48 )
        self.setHeight( 15 )
        self.speed = eelSpeed
    
    '''
    * Draws this eel onto the screen 
    '''
    def draw( self , screen ):
        Sprite.draw( self , screen )
        pass
    
    def updateSpeed(self, eelSpeed):
        self.speed = eelSpeed
    
    '''
    * TEMPORARY: The eel png is too tall (height too great). We need to offset
    * this by overriding the moveTo method to offset this extra height in
    * detecting collisions
    '''
    def moveTo( self , x , y ):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y+15
        
    '''
    * Moves the eel to the right by the speed of an eel
    '''
        
    def move(self, dx, dy):
        if (self.x + dx == 1000):
            self.EEL_SPEED = self.EEL_SPEED * -1
            self.moveTo( self.x , self.y + dy )
            self.flipImage()
        elif (self.x + dx == -500):
            self.EEL_SPEED = self.EEL_SPEED * -1
            self.moveTo( self.x , self.y + dy )
            self.flipImage()
        if (self.y + dy < 160):
            self.EEL_SHIFT = self.EEL_SHIFT * -1
        elif (self.y + dy > 500):
            self.EEL_SHIFT = self.EEL_SHIFT * -1
        self.moveTo( self.x + dx , self.y )
        
        
    def flipImage(self):
        self.image = pygame.transform.flip(self.image, 1, 0)
            
    def animate( self ):
        self.move( self.EEL_SPEED, 0 );
        
    '''
    *Checks to see if the eel has gone far off of the screen
    '''
    def isOutOfBounds( self ):    
        if (self.x > 500):
            print "yes"
            return True
        
    '''
    * Handles what happens when collision is detected
    '''
    def onCollide( self , otherSprite ):
        if ( isinstance( otherSprite , FishingHook ) ):
            self.stats.subtractLife()
#             ShockSound.play(1,0)
            #reset the fishing hook to start back at the surface
            #so that it doesn't keep colliding with  this eel
            self.fishingLine.resetLine()
            otherSprite.resetHook()
            pass
        elif ( isinstance( otherSprite , FishingLine ) ):
#             ShockSound.play(1,0)
            self.stats.subtractLife()
            otherSprite.resetLine()
            self.fishingHook.resetHook()
