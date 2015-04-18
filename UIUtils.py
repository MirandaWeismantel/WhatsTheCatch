'''
Created on Apr 7, 2015

@author: mjchao
'''

import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()


class Button(pygame.sprite.Sprite):
    def __init__(self , color , filename , location , size=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        if ( size != None ):
            self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey( color )
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
    def clicked( self , mouseX , mouseY ):
        return (self.rect.x <= mouseX and mouseX <= self.rect.x + self.rect.width) and \
                (self.rect.y <= mouseY and mouseY <= self.rect.y + self.rect.height)
                
class ButtonNoAlpha(pygame.sprite.Sprite):
    def __init__(self , color , filename , location , size=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        if ( size != None ):
            self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey( color )
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
    def clicked( self , mouseX , mouseY ):
        return (self.rect.x <= mouseX and mouseX <= self.rect.x + self.rect.width) and \
                (self.rect.y <= mouseY and mouseY <= self.rect.y + self.rect.height)
                
class Label( pygame.sprite.Sprite ):
    
    font = pygame.font.SysFont('Courier New', 20)
    forecolor = (0,0,0)
    borderVisible = True
    text = ""
    
    def __init__( self , location=(0,0) , size=(100,40) ):
        pygame.sprite.Sprite.__init__(self)
        self.backcolor = (255,255,255)
        self.size = size
        self.rectangle = pygame.Rect( 0 , 0 , size[ 0 ] , size[ 1 ] )
        self.image = pygame.Surface( size )
        
        self.rect = self.image.get_rect()
        self.rect.x = location[ 0 ]
        self.rect.y = location[ 1 ]
        self.rect.width = size[ 0 ]
        self.rect.height = size[ 1 ]
        
        self.redraw()
        
    def redrawRect( self ):
        self.image.fill( self.backcolor )
        if ( self.borderVisible ):
            pygame.draw.rect( self.image , (0,0,0) , self.rectangle , 1 )
        
    def setBorderVisible( self , visible ):
        self.borderVisible = visible
        self.redraw()
        
    def setFont( self , font ):
        self.font = font
        
    def setForecolor( self , forecolor ):
        self.forecolor = forecolor
        self.redraw()
        
    def setBackcolor( self , backcolor ):
        self.backcolor = backcolor
        self.redraw()
        
    def setText( self , text ):
        self.text = text
        self.redraw()
        
    def redraw(self):
        self.redrawRect()
        renderedText = self.font.render( self.text , 1 , self.forecolor )
        self.image.blit( renderedText , (10,10) )
        