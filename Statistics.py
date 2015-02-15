'''
Created on Feb 15, 2015

@author: mjchao
'''

'''
* Stores some information about the player's performance in the game.
* Specifically, the attributes stored are lives, points, number of completed
* sentences, and number of times the user has guessed incorrectly
'''
class Statistics:
    
    '''
    * number of lives the player has left
    '''
    lives = 0
    
    '''
    * number of points the player has earned
    '''
    points = 0
    
    '''
    * number of sentences the user has completed
    '''
    sentencesCompleted = 0
    
    '''
    * number of times the user has completed a sentence incorrectly
    '''
    incorrectCompletions = 0;
    
    '''
    * Creates a Statistics object with everything set at 0
    '''
    def __init__( self ):
        lives = 0
        points = 0
        sentencesCompleted = 0
        incorrectCompletions = 0
        
    '''
    * Gives the player an additional life
    '''
    def addLife( self ):
        self.lives += 1
        
    '''
    * Subtracts a life from the player
    '''
    def subtractLife( self ):
        self.lives -= 1
        
    '''
    * @return         number of lives the player has left
    '''
    def getLives( self ):
        return self.lives    
    
    '''
    * Adds some points to the player's score
    * 
    * @param amount     number of points to add
    '''
    def addPoints( self , amount ):
        self.points += amount
        
    '''
    * Subtracts some points from the player's score
    *
    * @param amount     number of points to subtract
    '''
    def subtractPoints( self , amount ):
        self.points -= amount
        
    '''
    * @return             the number of points the player has earned
    '''
    def getPoints( self ):
        return self.points
        
    '''
    * Adds 1 to the number of sentences the player has completed
    '''
    def incrementCompletedSentences( self ):
        self.sentencesCompleted += 1
     
    '''
    * @return             the number of sentences the user has completed
    '''   
    def getCompletedSentenceCount( self ):
        return self.sentencesCompleted
       
    '''
    * Adds 1 to the number of times the user incorrectly attempted to complete
    * a sentence
    ''' 
    def incrementIncorrectCompletions( self ):
        self.incorrectCompletions += 1
        
    '''
    * The number of sentences the user has completed incorrectly
    '''
    def getNumIncorrectCompletions( self ):
        return self.incorrectCompletions