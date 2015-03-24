'''
Created on Feb 15, 2015

@author: mjchao
'''

import pygame
from pygame.locals import *
from Image import Image


pygame.font.init()

'''
* Represents a word in a sentence
'''
class Word:
    
    '''
    * the textual representation of this word
    '''
    word = ""
    
    '''
    * Creates a word representing the given word
    *
    * @param word         the textual representation of the word, as a string
    '''
    def __init__( self , word ):
        self.word = word
      
    '''
    * Determines if this word is equal to another object. If the other object
    * is another word, then this compares the textual representation of this
    * word with the other word. If the other object is not a word, then 
    * this method returns False.
    *
    * @param otherObject  another object with which to compare this word
    * @return             if this word is equal to the given object
    '''  
    def equals( self , otherObject ):
        if isinstance( otherObject , Word ):
            return self.word == otherObject.word
        else:
            return False
    
    '''
    * @return         the textual representation of this word, as a string
    '''
    def toString( self ):
        return self.word

'''
* Represents a blank in the sentence
'''
class Blank:
    
    BLANK_TEXT = "_____"
    BLANK_TO_FILL_TEXT = "_"
    
    '''
    * a list of words that can be used to fill this blank
    '''
    acceptableWords = []
    
    '''
    * a list of words that cannot be used to fill this blank
    '''
    unacceptableWords = []
    
    '''
    * if this blank has been filled or not
    '''
    filled = False
    
    '''
    * the word used to fill in this blank
    '''
    filledWord = None
    
    '''
    * Represents a blank in a sentence that can be filled with any of the 
    * given acceptable words, but cannot be filled with any of the unacceptable
    * words
    *
    * @param acceptableWords         a list of words that the user could use
    *                                to fill in this blank
    * @param unacceptableWords       a lit of words that the user may not use
    *                                to fill in this blank
    '''
    def __init__( self , acceptableWords , unacceptableWords ):
        self.acceptableWords = acceptableWords
        self.unacceptableWords = unacceptableWords
        
    '''
    * Adds the given words to the list of acceptable words 
    *
    * @param words                   a list of acceptable words to add
    '''
    def addAcceptableWords( self , words ):
        for word in words:
            self.acceptableWords.append( word )
            
    '''
    * Adds the given words to the list of unacceptable words
    *
    * @param words                   a list of unacceptable words to add
    '''
    def addUnacceptableWords( self , words ):
        for word in words:
            self.unacceptableWords.append( word )
      
    '''
    * @return             if this blank has been filled with a word or not
    '''  
    def isFilled( self ):
        return self.filled
    
    '''
    * Attempts to fill in this blank with the given word
    * 
    * @param word         the word with which to try to fill this blank
    * @return             if the word was acceptable (True) or not (False)
    '''
    def tryToFillWith( self , word ):
        for acceptable in self.acceptableWords:
            if word.equals( acceptable ):
                self.filled = True
                self.filledWord = word
                
                size = [500, 500]
                screen = pygame.display.set_mode(size)
                
                bubble = Image(60, 40, 100, 100)
                bubble.setImage(pygame.image.load( "res/correct.png" ).convert())
                bubble.draw(screen)
                return True
            
        for unacceptable in self.unacceptableWords:
            if word.equals( unacceptable ):
                self.filled = False
                return False
            
        return False 
    
    '''
    * @return             the word with which this blank is filled, or None
    *                     if this blank is not yet filled
    '''   
    def getFilledWord( self ):
        return self.filledWord
    
    def toString( self ):
        if ( self.isFilled() ):
            return self.filledWord.toString()
        else:
            return self.BLANK_TEXT
        
'''
* Represents a sentence that the user will have to complete
'''
class Sentence:
    
    '''
    * the sequence of words and blanks from which this sentence is composed
    '''
    sequence = []
    
    '''
    * the font with which this sentence is displayed
    '''
    sentenceFont = pygame.font.SysFont( "Courier New" , 18 )

    '''
    * the font with which to fill in blanks
    '''    
    fillInFont = pygame.font.SysFont( "Courier New" , 120 )
    
    '''
    * how this sentence is punctuated
    '''
    punctuation = "."
    
    '''
    * Creates a sentence with the given sequence of words and blanks
    *
    * @param sequence         a sequence of words and blanks from which this
    *                         sentence is compose
    * @param punctuation      how the sentence is punctuated
    '''
    def __init__( self , sequence , punctuation ):
        self.sequence = sequence

    '''
    * @return             if this sentence is complete, that is, if it has
    *                     any more blanks left to be filled
    '''
    def isComplete( self ):
        for component in self.sequence:
            if isinstance( component , Blank ):
                if not component.isFilled():
                    return False
                
        return True
        
    '''
    * Attempts to fill in the next blank with the given word
    *
    * @param word         the word with which to try to fill in the next blank
    * @return             if the provided word is an acceptable fit for the next
    *                     blank in this sentence
    '''
    def fillInNextBlank( self , word ):
        for component in self.sequence:
            if isinstance( component , Blank ):
                if not component.isFilled():
                    return component.tryToFillWith( word )
                
        raise Exception( "No more blanks to fill! " + 
                            "Check if sentence is complete first!" );
            
    '''
    * Creates a list of words that cannot be used to fill in the next blank
    *
    * @return             a list of words unacceptable words for filling in
    *                     the next blank
    '''                
    def getUnacceptableWordsForNextBlank( self ):
        for component in self.sequence:
            if ( isinstance( component , Blank ) ):
                if ( not component.isFilled() ):
                    return component.unacceptableWords
                
    '''
    * @return             a list of acceptable words that can be used to fill 
    *                     in the first unfilled blank
    '''
    def getAcceptableWordsForNextBlank( self ):
        for component in self.sequence:
            if isinstance( component , Blank ):
                if not component.isFilled():
                    return component.acceptableWords
      
    '''
    * @return             the textual representation of this sentence
    *                     as it should be displayed on the game screen
    '''
    def toString( self ):
        rtn = ""
        for component in self.sequence:
            rtn += " " + component.toString()
            
        return rtn.strip() + self.punctuation
    
    def deleteWords(self):
        del Blank.acceptableWords[:]
        del Blank.unacceptableWords[:]
    
    '''
    * Draws this sentence onto the screen
    *
    * @param screen         where to draw this sentence and its blank
    '''                      
    def draw( self , screen ):
        entireText = self.toString()
        
        #determine if we need to draw the text separately or not, as
        #the first blank that the user needs to fill in must be in bold red,
        #but we must render text of different size and font separately
        idxOfFirstBlank = entireText.find( Blank.BLANK_TEXT )
        
        #if the first blank does not exist, then it's very easy for 
        #us to render
        if ( idxOfFirstBlank == -1 ) :
            textToFirstBlank = entireText
            textOfFirstBlank = ""
            textToEnd = ""
            
        #if the first blank exists, we have divide the text up into the part
        #before the blank, the first blank, and the part after the first blank
        else:
            textToFirstBlank = entireText[ 0 : idxOfFirstBlank ]
            textOfFirstBlank = Blank.BLANK_TO_FILL_TEXT
            textToEnd = entireText[ idxOfFirstBlank + len( Blank.BLANK_TEXT ) : 
                                                            len( entireText ) ]
        
        #render the text before the first blank
        display1 = self.sentenceFont.render( textToFirstBlank , 1 , 
                                                    [0 , 0 , 0] )
        
        #calculate the dimensions of the text before the first blank
        width1 = self.sentenceFont.size( textToFirstBlank )[ 0 ]
        height1 = self.sentenceFont.size( textToFirstBlank )[ 1 ]
        
        #render the text of the first blank in red and with a large, thick font
        displayBlank = self.fillInFont.render( textOfFirstBlank , 1 , 
                                                    [ 255, 0 , 0 ] )
        
        #calculate the dimensions of the text of the first blank 
        widthBlank = self.fillInFont.size( textOfFirstBlank )[ 0 ]
        heightBlank = self.fillInFont.size( textOfFirstBlank )[ 1 ]
        
        #render the text after the first blank
        display3 = self.sentenceFont.render( textToEnd , 1 , [ 0 , 0 , 0 ] )
        
        #blitting the text before the first blank is easy, we just draw it
        #where is should start
        screen.blit( display1 , (10 , 50 ) )
        
        #we have to calculate offsets to render the text of the first blank - 
        #particularly, it is width1 to the left of its previous text
        #but since the font is also really big to get thickness, the underscore
        #also appears much lower than the rest of the text. We have to offset
        #this by blitting this underscore higher
        #
        #the extra 3 offset on the height is there to help even it out with
        #the height of other blanks and look nice
        screen.blit( displayBlank , (10 + width1 , 50 - 
                                     (heightBlank - height1 ) + 3 ) )
        
        #blitting the text after the first blank is straightforward.
        #we just offset it by the width of the text up to and including the
        #first blank
        screen.blit( display3 , (10 + width1 + widthBlank , 50 ) )

        