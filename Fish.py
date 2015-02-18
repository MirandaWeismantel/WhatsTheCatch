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
    
    '''
    * the speed of the fish before it was hooked. This way, if the fish gets
    * unhooked (i.e. the hook touches an eel), the fish continues swiming
    * in the correct direction
    '''
    lastFishSpeed = 1
    
    fishShift = 50
    caught = False
    hooked = False
    
    '''
    * if the fish is facing right
    '''
    facingRight = True
    
        
    def __init__( self, word ):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        self.setImage( pygame.image.load( "res/fish.png" ).convert() );
        self.hooked = False
        self.word = word
        self.setWidth( 32 )
        self.setHeight( 25 )
        pass
    
    '''
        * Draws this fish onto the screen
        '''
    def draw( self , screen ):
        self.key_press()
        Sprite.draw( self , screen )
        self.drawWord( screen )
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
            if ( otherSprite.canHookFish( self ) ):
                self.hook()
        
    '''
    * Draws the word on to the fish
    '''
    def drawWord( self , screen ):
        font = pygame.font.SysFont('Courier New', 15)
        text = font.render(self.word.toString(), True, (0, 0, 0))
        screen.blit(text, (self.rect.x+10 , self.rect.y+15) )
            
            
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
                if (self.y - dist <125):
                    self.y = 20
                    self.x = 0
                    self.hooked = False
                    self.caught = True
                else:   
                    self.y -= dist # move right
            elif key[pygame.K_DOWN]: # left key
                if (self.y + dist >490):
                    self.y = self.y
                else:   
                    self.y += dist # move left
                    
    def flipImage(self):
        self.facingRight = not self.facingRight
        self.image = pygame.transform.flip(self.image, 1, 0)
        
    def hook( self ):
        #TODO
        self.fishSpeed = 0
        self.hooked = True
        
    def unhook(self):
        if ( self.facingRight ):
            self.fishSpeed = 1
        else:
            self.fishSpeed = -1
        
        self.hooked = False
