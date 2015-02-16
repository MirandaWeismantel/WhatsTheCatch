'''
Created on Feb 15, 2015

@author: mjchao
'''

import pygame
from pygame.locals import *

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
    '''
    def tryToFillWith( self , word ):
        for acceptable in self.acceptableWords:
            if word.equals( acceptable ):
                self.filled = True
                self.filledWord = word
                return True
            
        for unacceptable in self.unacceptableWords:
            if word.equals( unacceptable ):
                self.filled = False
                return False
            
        raise Exception( 'Unknown word used to fill in blank: ' + 
                                                            word.toString() )
     
    '''
    * @return             the word with which this blank is filled, or None
    *                     if this blank is not yet filled
    '''   
    def getFilledWord( self ):
        return self.filledWord
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
    sentenceFont = pygame.font.SysFont( "Courier New" , 15 )
    
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
    * @return             the textual representation of this sentence
    *                     as it should be displayed on the game screen
    '''
    def toString( self ):
        rtn = ""
        for component in self.sequence:
            if isinstance( component , Word ):
                rtn += " " + component.toString()
            elif isinstance( component , Blank ):
                if ( component.isFilled() ):
                    rtn += " " + component.getFilledWord().toString()
                else:
                    rtn += " _____"
            
        return rtn.strip() + self.punctuation
    
    '''
    * Draws this sentence onto the screen
    *
    * @param screen         where to draw this sentence and its blank
    '''                      
    def draw( self , screen ):
        textDisplay = self.sentenceFont.render( self.toString() , 1 , 
                                                    [0 , 0 , 0] )
        screen.blit( textDisplay , (10 , 10) )