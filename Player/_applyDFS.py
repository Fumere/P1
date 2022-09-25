# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:38:55 2022

@author: neelkh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 02:44:55 2022

@author: dharmendrakhakhar
"""
import numpy as np
def applyDFS(self):
    
    
    
    def AppSeq(self):
        
        currLoc = self.currState.currLoc
        
        # print('curr loc is ',currLoc)
        possMovsMaybe = self.heur + np.array(currLoc)
        possMovsMaybe = possMovsMaybe[(possMovsMaybe>-1).all(axis=1),:]
        possMovsMaybe = possMovsMaybe[(possMovsMaybe<len(self.currState.boardObj.board)).all(axis=1),:]
        # print('maybe moves 1 ', possMovsMaybe)
        possMovsValidTruth = self.currState.isBanned(possMovsMaybe)
        possMovsValid = possMovsMaybe[possMovsValidTruth,:]
        # print('valid moves', possMovsValid)
        
        return possMovsValid
    
       
    
    
    def updatePossMoves(self, possMovsValid):
        
        #Frontier
        
        # self.currState.board[tuple(newPossMoves.T)] = np.arange(self.stepCount+1,self.stepCount+len(newPossMoves)+1,1)
        possMovsValid = possMovsValid.tolist()
        newPossMoves =[]
        for i in possMovsValid:
            if i not in self.currState.possMoves:
                newPossMoves.append(i)
        
        self.currState.possMoves = self.currState.possMoves + newPossMoves
        return newPossMoves
                
        
                
    def getNextMoveL(self):
        
        allPossMoves = self.currState.possMoves
        nextLoc = allPossMoves[len(allPossMoves)-1]
        self.currState.possMoves = self.currState.possMoves[0:len(allPossMoves)-1]
        # self.currState.possMoves = allPossMoves[np.all(allPossMoves != nextLoc, axis =1),:]
        return nextLoc
    
    def updateBoard(self, newPossMoves):
        
        if len(newPossMoves):
            newPossMoves = np.array(newPossMoves)
            self.currState.boardObj.board[tuple(newPossMoves.T)] = np.arange(self.stepCount+1,self.stepCount+len(newPossMoves)+1,1)
            self.stepCount = self.stepCount+len(newPossMoves)
    
        
    ######                    
                
    possMovsValid = AppSeq(self) #branches
    newPossMoves = updatePossMoves(self, possMovsValid)
    updateBoard(self, newPossMoves)
    # print('all curr poss locs \n', self.currState.possMoves)
    nextLoc = getNextMoveL(self)
    # print('next loc is ',nextLoc)
    return nextLoc   