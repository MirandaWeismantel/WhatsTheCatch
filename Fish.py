'''
    Created on Feb 13, 2015
    
    @author: weismant
    '''

import pygame
from Sprite import Sprite
from FishingHook import FishingHook

class Fish( Sprite ):
    
    '''
        * How fast the Fish moves per tick of the pygame clock. This quantity is
        * in pixels
        '''
    fishSpeed = 1
    fishShift = 50
    
        
    def __init__( self ):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/fish.png" ).convert() );
        self.hooked = False
        self.setHeight( 25 )
        pass
    
    '''
        * Draws this fish onto the screen
        '''
    def draw( self , screen ):
        self.key_press()
        Sprite.draw( self , screen )
        pass
    
    '''
        * Draws this fish onto the screen
        '''
    def move(self, dx, dy):
        if (self.x + dx == 600):
            self.fishSpeed = self.fishSpeed * -1
            self.moveTo( self.x , self.y + dy )
            self.flipImage()
        elif (self.x + dx == -100):
            self.fishSpeed = self.fishSpeed * -1
            self.moveTo( self.x , self.y + dy )
            self.flipImage()
        if (self.y + dy < 160):
            self.fishShift = 50
        elif (self.y + dy > 500):
            self.fishShift = -50
        self.moveTo( self.x + dx , self.y )
        
    
    '''
        * Moves the fish to the right by the speed of a fish
        '''
    def animate( self ):
        self.move( self.fishSpeed , self.fishShift );
    
    '''
        * Handles what happens when collision is detected
        '''
    def onCollide( self , otherSprite ):
        if ( isinstance( otherSprite , FishingHook ) ):
            self.fishSpeed = 0
            self.hooked = True
            
    def key_press(self):
        """ Handles Keys """
        if(self.hooked == True):
            key = pygame.key.get_pressed()
            dist = 1
            if key[pygame.K_RIGHT]: # right key
                self.x += dist # move right
            elif key[pygame.K_LEFT]: # left key
                self.x -= dist # move left
            if key[pygame.K_UP]: # right key
                if (self.y - dist <120):
                    self.y = 20
                    self.x = 0
                    self.hooked = False
                else:   
                    self.y -= dist # move right
            elif key[pygame.K_DOWN]: # left key
                if (self.y + dist >490):
                    self.y = self.y
                else:   
                    self.y += dist # move left
                    
    def flipImage(self):
        self.image = pygame.transform.flip(self.image, 1, 0)
