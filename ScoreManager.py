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
            factory = SentenceFactory( filename )
            factory.load()
            maxPoints = factory.getMaxPoints()
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
            print "Updated " + filename + ": " + str(bestScore) + " " + str(maxPoints)
            data.bestScore = max( data.bestScore , bestScore )
            data.maxPoints = maxPoints
            
def getScoreFor( filename ):
    for data in scoreData :
        if ( data.filename == filename ):
            return data.bestScore
        
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
        