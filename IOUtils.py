'''
Created on Mar 6, 2015

@author: mjchao
'''

'''
* Reads files line by line
'''
class BufferedReader:
    
    '''
    * the current line the reader is at in the buffer
    '''
    lineIdx = 0
    
    '''
    * the buffer that stores the lines of a file
    '''
    lines = []
    
    '''
    * Creates a BufferedReader object to read through the given file
    * line by line
    *
    * @param filename         the file to be read
    '''
    def __init__( self , filename ):
        self.lines = open( filename , 'r' ).read().splitlines()
        
    '''
    * @return             if the end of the file has been reached
    '''
    def eof( self ):
        return self.lineIdx == len( self.lines )
    
    '''
    * Reads the next line in the file, assuming that eof has not been reached.
    * If eof has been reached, then this will cause an error. 
    *
    * @return             the next line in the file
    '''
    def readLine( self ):
        rtn = self.lines[ self.lineIdx ]
        self.lineIdx += 1
        return rtn
    
'''
* Turns a string into tokens using a given delimiter
'''    
class StringTokenizer:
    
    '''
    * current processed token
    '''
    tokenIdx = 0
    
    '''
    * the list of tokens contained by this tokenizer
    '''
    tokens = []
    
    '''
    * Creates a StringTokenizer that splits the given string into individual
    * tokens using the given delimiter
    *
    * @param string         the string to tokenize
    * @param delimiter      the delimiter that separates tokens. Use None
    *                       to tokenize by whitespace
    '''
    def __init__( self , string , delimiter = None ):
        if ( delimiter == None ):
            self.tokens = string.split()
        else:
            self.tokenIdx = string.split( delimiter )
        
    '''
    * @return             if there are anymore tokens left in this tokenizer
    '''
    def hasNext( self ):
        return self.tokenIdx != len( self.tokens )
    
    '''
    * Gets and removes the next token in the sequence
    *
    * @return             the next token in the sequence
    '''
    def nextToken( self ):
        rtn = self.tokens[ self.tokenIdx ]
        self.tokenIdx += 1
        return rtn
