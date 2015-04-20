'''
Created on Apr 7, 2015

@author: mjchao
'''

from IOUtils import BufferedReader , PrintWriter
from SentenceFactory import SentenceFactory

class SentenceFileScore:
    
    filename = ""
    bestScore = 0
    maxPoints = 0
    
    def __init__( self , filename , bestScore = None , maxPoints = None ):
        self.filename = filename
        if ( maxPoints == None ):
            factory = SentenceFactory( "sentences/" + filename )
            factory.load()
            factory.validate()
            self.maxPoints = factory.getMaxPoints()
        else:
            self.maxPoints = maxPoints
            
        if ( bestScore == None ):
            self.bestScore = 0
        else:
            self.bestScore = bestScore
        
scoreData = []

def initialize():
    global scoreData
    scoreData = []
    f = BufferedReader( "data/score" )
    while( not f.eof() ):
        filename = f.readLine()
        if filename.strip() == "":
            break
        bestScore = int( f.readLine() )
        maxPoints = int( f.readLine() )
        scoreData.append( SentenceFileScore( filename , bestScore , maxPoints ) )

    

def saveScores():
    global scoreData
    
    out = PrintWriter( "data/score" )
    for data in scoreData :
        out.writeln( data.filename )
        out.writeln( data.bestScore )
        out.writeln( data.maxPoints )
        
def updateScore( filename , bestScore , maxPoints ):
    global scoreData
    for data in scoreData :
        if ( data.filename == filename ):
            data.bestScore = max( data.bestScore , bestScore )
            data.maxPoints = maxPoints
            saveScores()
            return
        
    newSentenceData = SentenceFileScore( filename , bestScore , None )
    for i in range(0, len(scoreData) ):
        if filename < scoreData[ i ].filename:
            scoreData.insert( i , newSentenceData )
            saveScores()
            return
        
    scoreData.append( newSentenceData )
    saveScores()
    return
            
def getScoreFor( filename ):
    for data in scoreData :
        if ( data.filename == filename ):
            return data.bestScore
     
    newSentenceData = SentenceFileScore( filename , 0 , None )
    for i in range(0, len(scoreData) ):
        if filename < scoreData[ i ].filename:
            scoreData.insert( i , newSentenceData )
            return 0
        
    scoreData.append( newSentenceData )
    return 0
        
def getMaxPointsFor( filename ):
    for data in scoreData:
        if ( data.filename == filename ):
            return data.maxPoints
            
def getNumSetsMastered():
    global scoreData
    rtn = 0
    for data in scoreData:
        if ( data.bestScore == data.maxPoints ):
            rtn += 1
    return rtn

def getTotalSets():
    return len( scoreData )
        