'''
Created on Mar 6, 2015

@author: mjchao
'''

import random
from Sentence import Sentence , Blank , Word
from IOUtils import BufferedReader , StringTokenizer
    
'''
* Stores data about a sentence. Specifically, it contains the Sentence
* object representation, the filename from which the sentence data was read
* and the data and line number from the file corresponding to the sentence. 
* 
* This class should not be exported from this file
'''
class SentenceData:
    
    def __init__( self , sentence , filename , data , lineNumber ):
        self.sentence = sentence
        self.filename = filename
        self.data = data
        self.lineNumber = lineNumber

'''
* Reads in sentence data from a factory and provides a convenient way of 
* generating sentences for the game.
'''
class SentenceFactory:
    
    '''
    * the list of sentences this factory contains 
    '''
    sentences = []
    
    '''
    * the filename in which sentence data is stored
    '''
    filename = ""
    
    '''
    * Loads sentence data into this factory. This method is not to be called
    * outside this class
    '''
    def load( self ):
        f = BufferedReader( self.filename )
        
        #keep track of line numbers, which can be used to display
        #error messages about bad data files
        lineNumber = 0
        
        #scan through the entire file
        while( not f.eof() ):
            nextLine = f.readLine()
            lineNumber += 1
            
            #check if the line is a comment/whitespace of if it contains some
            #sentence data. Sentence data is always on its own line
            #and starts with the "Sentence:" identifier
            if ( nextLine.startswith( "Sentence:" ) ):
                sentenceComponents = []
                st = StringTokenizer( nextLine )
                
                #discard the "Sentence:" token
                st.nextToken()
                
                #indicate whether we are reading in words from a sentence
                #or words that belong to blanks in a sentence
                readingBlank = False
                readingBlankValid = False
                blankValidWords = []
                blankInvalidWords = []
                
                while( st.hasNext() ):
                    nextToken = st.nextToken()
                    if ( readingBlank ):
                        
                        #"]" denotes that the end of the list of words for the
                        #given blank has been reached.
                        if ( nextToken == "]" ):
                            readingBlank = False
                            sentenceComponents.append( Blank( blankValidWords , 
                                                        blankInvalidWords ) )
                            blankValidWords = []
                            blankInvalidWords = []
                            
                        #"|" separates the valid and invalid words that can
                        #be used to fill in a blank
                        elif ( nextToken == "|" ):
                            readingBlankValid = False
                        else:
                            if ( readingBlankValid ):
                                blankValidWords.append( Word( nextToken ) )
                            else :
                                blankInvalidWords.append( Word( nextToken ) )   
                    else:
                        
                        #"[" indicates the start of a blank and the words
                        #that can be used to fill it
                        if ( nextToken == "[" ):
                            readingBlank = True
                            readingBlankValid = True
                        else:
                            sentenceComponents.append( Word( nextToken ) )
                
                #last token would be the punctuation
                punctuation = sentenceComponents[ len( sentenceComponents ) - 1 ]
                sentenceComponents.remove( punctuation )
                
                #create an add the sentence to the sentence factory's 
                #master list of sentences
                self.sentences.append( SentenceData( 
                    Sentence( sentenceComponents , punctuation.toString() ) , 
                    self.filename , nextLine , lineNumber ) )
                        
            else:
                #ignore comments and whitespace
                pass
    
    '''
    * Creates a sentence factory that will take data from the given file
    *
    * @param filename         the file with sentence data
    '''
    def __init__( self , filename ):
        self.filename = filename
        self.sentences = []
        self.load()
        
    
    '''
    * @return             if there are any more sentences left in this
    *                     SentenceFactory
    '''    
    def hasMoreSentences( self ):
        return len( self.sentences ) != 0
    
    '''
    * Gets a random sentence that hasn't been used yet. This will cause an
    * error if all the sentences have already been used.
    *
    * @return             a random sentence that has not yet been used
    '''
    def next( self ):
        randSentence = random.choice( self.sentences )
        self.sentences.remove( randSentence )
        return randSentence.sentence
   
    '''
    * Checks if all the sentences seem valid
    '''
    def validate( self ):
        print "Validating \"" + self.filename + "\""
        for sentenceData in self.sentences:
            text = sentenceData.sentence.toString()
            if ( "[" in text or "]" in text or "|" in text ):
                print "Check sentence: \"" + sentenceData.data + "\" in " + \
                        sentenceData.filename + " ... line " + \
                        str( sentenceData.lineNumber )
        print "Finished Validating \"" + self.filename + "\""
        