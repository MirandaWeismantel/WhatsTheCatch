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
    fishSpeedOld = fishSpeed
    
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
    
    
        
    def __init__( self, word, speed ):
        Sprite.__init__( self , 32 , 32 , 0 , 0 )
        #self.image1=pygame.image.load("Fish/Fish1.png")
        self.image2=pygame.image.load("Fish/Fish2.png")
        #self.image3=pygame.image.load("Fish/Fish3.png")
        self.hooked = False
        self.word = word
        font = pygame.font.SysFont('Courier New', 15)
        text = font.render(self.word.toString(), True, (255, 255, 0))
        textpos=text.get_rect()
        textwidth = tuple(textpos)[2]
        self.image2.set_colorkey( (0,0,0) )
        self.setImage( pygame.transform.scale((self.image2),(textwidth+10,32)));
        self.setWidth( textwidth)
        self.setHeight( 25 )
        #self = pygame.transform.scale(self, (1200,800))
        self.fishSpeed = speed
        pass
    
    '''
        * Draws this fish onto the screen
        '''
    def draw( self , screen ):
        self.key_press()
        Sprite.draw( self , screen )
        self.drawWord( screen )
        pass
    
            
    def setOldSpeed(self, speed):
        self.fishSpeedOld = speed
          
    
    def updateSpeed(self, speed):
        if ( self.fishSpeed < 0 ) :
            self.fishSpeed = -1*speed
        else:
            self.fishSpeed = speed
        
    def moveTo( self , x , y ):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y#-7
        #
    '''
        * Draws this fish onto the screen
        '''
    def move(self, dx, dy):
        if (self.x + dx >= 600 and self.facingRight):
            self.fishSpeed = self.fishSpeed * -1
            self.moveTo( self.x , self.y + dy )
            self.flipImage()
        elif (self.x + dx <= -100 and not self.facingRight):
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
                if ( self.fishSpeed != 0):
                    self.setOldSpeed(self.fishSpeed)
                self.hook()
    
        
    '''
    * Draws the word on to the fish
    '''
    def drawWord( self , screen ):
        font = pygame.font.SysFont('Courier New', 15)
        font.set_bold(True)
        text = font.render(self.word.toString(), True, (255, 255, 255))
        screen.blit(text, (self.x+0 , self.y+5) )
        textpos=text.get_rect()
        textwidth = tuple(textpos)[2]
        self.setWidth( textwidth)
        
        
        
            
            
    def key_press(self):
        """ Handles Keys """
        if(self.hooked == True):
            key = pygame.key.get_pressed()
            dist = 1
            if key[pygame.K_UP]: # right key
                if (self.y - dist <125):
                    self.y = 20
                    self.x = 0
                    self.hooked = False
                    self.caught = True
            if key[pygame.K_SPACE]:
                self.unhook()
                
                
                    
    def flipImage(self):
        self.facingRight = not self.facingRight
        self.image = pygame.transform.flip(self.image, 1, 0)
        
    def hook( self ):
        self.fishSpeed = 0
        self.hooked = True
        
    def unhook(self):
        newY = max( self.y + 20 , 180 )
        self.moveTo(self.x, newY)
        #print(self.fishSpeedOld)
        self.fishSpeed = self.fishSpeedOld
        
        #if ( self.facingRight ):
            #self.fishSpeed = self.fishSpeedOld
        #else:
            #self.fishSpeed = self.fishSpeedOld
        
        
        self.hooked = False
