'''
Created on Apr 7, 2015

@author: mjchao
'''

import os

class SentenceListManager:
    
    SENTENCE_DIRECTORY = "sentences"
    
    currIdx = 0
    
    def __init__( self ):
        self.filenames = next(os.walk( self.SENTENCE_DIRECTORY ) )[ 2 ]
        if ( len( self.filenames ) == 0 ):
            raise "Could not locate sentence data!"
        
    def next(self):
        self.currIdx = (self.currIdx + 1) % len( self.filenames )
        
    def prev(self):
        self.currIdx = (self.currIdx - 1) % len( self.filenames )
        
    def getSelectedFilename(self):
        return self.filenames[ self.currIdx ]
    
    def getAllDirectories( self ):
        return self.filenames