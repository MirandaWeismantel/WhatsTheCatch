'''
Created on Feb 12, 2015

@author: mjchao
'''

import pygame
from pygame.locals import *

'''
* Represents an Image in the game. While there is nothing preventing one from
* modifying the appearance and position, Images should be static in position 
* and unchanging in appearance throughout the game.
'''
class Image( pygame.sprite.Sprite ):
    
    '''
    * x coordinate of the Image on the screen, in pixels. The x coordinate
    * is the x value of the top, left corner of the Image.
    *
    * This should be
    * set in the constructor, but never changed afterwards, since the Image is 
    * static
    '''
    x = 0
    
    '''
    * y coordinate of the Image on the screen, in pixels. The y coordinate
    * is the y value of the top, left corner of the Image.
    *
    * This should be set in the constructor, but never changed afterwards, 
    * since the Image is static
    '''
    y = 0
    
    '''
    * the width (span in the x direction) of the Image on the screen, in pixels.
    * This should be set in the constructor, but never changed afterwards,
    * since the Image is unchanging in appearance
    '''
    width = 0
    
    '''
    * the height (span in the y direction) of the Image on the screen, in 
    * pixels. This should be set in the constructor, but never changed
    * afterwards, since the Image is unchanging in appearance
    '''
    height = 0
    
    '''
    * Draws the image onto the screen. This must be implemented in subclasses.
    '''
    def draw( self ):
        pass
    
    '''
    * @return          a pair, [x, y], representing the x and y coordinates of
    *                  the location of this sprite in pixels.
    '''
    def getLocation( self ):
        return [self.x, self.y]
        
    '''
    * Sets the width of the bounding box of this Image. The width is the 
    * image's span in the x-direction
    *
    * @param width            the width of the bounding box of this image,
    *                         in pixels
    '''
    def setWidth( self , width ):
        self.width = width
        
    '''
    * Sets the height of the bounding box of the Image. The height is the
    * image's span in the y-direction
    *
    * @param height            the height of the bounding box of this image,
    *                          in pixels
    '''
    def setHeight( self , height ):
        self.height = height
        
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
    
    