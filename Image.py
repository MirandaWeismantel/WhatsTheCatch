'''
Created on Feb 12, 2015

@author: mjchao
'''

import pygame
from pygame.locals import *

'''
* Represents an Image in the game.
'''
class Image( pygame.sprite.Sprite ):
    
    '''
    * x coordinate of the Image on the screen, in pixels. The x coordinate
    * is the x value of the top, left corner of the Image. Do not modify this
    * value directly.
    '''
    x = 0
    
    '''
    * y coordinate of the Image on the screen, in pixels. The y coordinate
    * is the y value of the top, left corner of the Image. Do not modify this
    * value directly.
    '''
    y = 0
    
    '''
    * the width (span in the x direction) of the Image on the screen, in pixels.
    * Do not modify this value directly - use setWidth() instead
    '''
    width = 0
    
    '''
    * the height (span in the y direction) of the Image on the screen, in 
    * pixels. Do not modify this value directly - use setHeight() instead 
    '''
    height = 0
    
    '''
    * the bounding rectangle of this Image. This is the bounding rectangle from
    * pygame.sprite.Sprite used for detecting collisions. Do not modify this 
    * value. It should be handled solely by the Image object
    '''
    rect = None
    
    '''
    * the image to be displayed by this Image in its draw method. Do not modify
    * this value directly - use setImage() instead.
    '''
    image = None
    
    '''
    * Creates an image with the given width and height and sets it at the
    * given location (x, y)
    *
    * @param width     width of the image in pixels
    * @param height    height of the image in pixels
    * @param x         x coordinate of the image in pixels
    * @param y         y coordinate of the image in pixels
    '''
    def __init__( self , width , height , x , y ):
        pygame.sprite.Sprite.__init__( self )
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    '''
    * Draws the image onto the screen. This must be implemented in subclasses.
    *
    * @param screen     the screen onto which to draw this image
    '''
    def draw( self , screen ):
        if ( self.image != None ):
            screen.blit( self.image , (self.x , self.y ) )
    
    '''
    * @return          a pair, [x, y], representing the x and y coordinates of
    *                  the location of this sprite in pixels.
    '''
    def getLocation( self ):
        return [self.x, self.y]
    
    '''
    * Sets the image to be displayed
    * 
    * @param image         the image to be displayed. 
    '''
    def setImage( self , image ):
        self.image = image;
        self.image.set_colorkey( (255, 255, 255) )
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.width = self.rect.width
        self.height = self.rect.height
            
    '''
    * Sets the width of the bounding box of this Image. The width is the 
    * image's span in the x-direction
    *
    * @param width            the width of the bounding box of this image,
    *                         in pixels
    '''
    def setWidth( self , width ):
        self.width = width
        self.rect.width = width;
        
    '''
    * Sets the height of the bounding box of the Image. The height is the
    * image's span in the y-direction
    *
    * @param height            the height of the bounding box of this image,
    *                          in pixels
    '''
    def setHeight( self , height ):
        self.height = height
        self.rect.height = height;
        
    '''
    * @return                 the width of the bounding box of this image,
    *                         in pixels
    '''      
    def getWidth( self ):
        return self.width
    
    '''
    * @return                 the height of the bounding box of this image,
    *                         in pixels
    '''
    def getHeight( self ):
        return self.height
    
    