'''
Created on Apr 7, 2015

@author: mjchao
'''

import pygame
from pygame.locals import *

class Button(pygame.sprite.Sprite):
    def __init__(self , color , filename , location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (100,40))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
    def clicked( self , mouseX , mouseY ):
        return (self.rect.x <= mouseX and mouseX <= self.rect.x + self.rect.width) and \
                (self.rect.y <= mouseY and mouseY <= self.rect.y + self.rect.height)