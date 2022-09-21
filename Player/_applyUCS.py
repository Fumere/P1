# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:56:07 2022

@author: neelkh
"""

import numpy as np
def applyUCS(self):
    
    
    
    def AppSeq(self):
        
        currLoc = self.currState.currLoc
        
        print('curr loc is ',currLoc)
        possMovsMaybe = self.heur + np.array(currLoc)
        UCSOrdered = UCSorder(self, possMovsMaybe )
        
        possMovsMaybe = UCSOrdered[(UCSOrdered>-1).all(axis=1),:]
        possMovsMaybe = possMovsMaybe[(possMovsMaybe<len(self.currState.board)).all(axis=1),:]
        print('maybe moves 1 ', possMovsMaybe)
        possMovsValid = self.currState.isBanned(possMovsMaybe)
        print('valid moves', possMovsValid)
        
        return possMovsValid
    
       
    
    def UCSorder(self, possMovsMaybe):
            
        arrIndices = np.array(self.customHeur).argsort()
        
        possMovsMaybeOrdered= possMovsMaybe[arrIndices[::1]]
        
        return possMovsMaybeOrdered
  
            
    def updatePossMoves(self, possMovsValid):
        
        #Frontier
        
        # self.currState.board[tuple(newPossMoves.T)] = np.arange(self.stepCount+1,self.stepCount+len(newPossMoves)+1,1)
        possMovsValid = possMovsValid.tolist()
        newPossMoves =[]
        for i in possMovsValid:
            if i not in self.currState.possMoves:
                newPossMoves.append(i)
        
        self.currState.possMoves = newPossMoves + self.currState.possMoves
        return newPossMoves
                
        
                
    def getNextMoveL(self):
        
        allPossMoves = self.currState.possMoves
        nextLoc = allPossMoves[0]
        self.currState.possMoves = self.currState.possMoves[1:]
        # self.currState.possMoves = allPossMoves[np.all(allPossMoves != nextLoc, axis =1),:]
        return nextLoc
    
    def updateBoard(self, newPossMoves):
        
        if len(newPossMoves):
            newPossMoves = np.array(newPossMoves)
            self.currState.board[tuple(newPossMoves.T)] = np.arange(self.stepCount+1,self.stepCount+len(newPossMoves)+1,1)
            self.stepCount = self.stepCount+len(newPossMoves)
    
        
    ######                    
                
    possMovsValid = AppSeq(self) #branches
    newPossMoves = updatePossMoves(self, possMovsValid)
    updateBoard(self, newPossMoves)
    print('all curr poss locs \n', self.currState.possMoves)
    nextLoc = getNextMoveL(self)
    print('next loc is ',nextLoc)
    return nextLoc   