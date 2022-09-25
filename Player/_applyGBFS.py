#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 22:23:51 2022

@author: dharmendrakhakhar
"""


import numpy as np

def applyGBFS(self):
    
    
    
    def AppSeq(self):
        
        currLoc = self.currState.currLoc
        # print('curr loc is ',currLoc)
        possMovsMaybe = self.heur + np.array(currLoc)
        
        possMovsMaybeTruth = np.logical_and((possMovsMaybe>-1).all(axis=1), (possMovsMaybe<len(self.currState.boardObj.board)).all(axis=1))

        # print('maybe moves 1 ', possMovsMaybe[possMovsMaybeTruth,:])
        possMovsValidTruth = self.currState.isBanned(possMovsMaybe)
        
        totalTruth = np.logical_and(possMovsMaybeTruth , possMovsValidTruth)
        
        costsOfPossMoves = getGBFSCost(self, possMovsMaybe)
        
        possMovsValid = possMovsMaybe[totalTruth,:]
        costsOfPossMoves = costsOfPossMoves [totalTruth ]
        
        # print('valid moves', possMovsValid)
        # print('costs of moves', costsOfPossMoves)
        
        return [possMovsValid, costsOfPossMoves]
    
    def getGBFSCost(self, possMovsMaybe):
        
        dist = self.currState.boardObj.endLoc - possMovsMaybe
        costs = []
        
        for i in dist:
            cost = 0
            if i[0]>0:
                cost += i[0]*self.customHeur[2]
            elif i[0]<0:
                cost += abs(i[0]*self.customHeur[0])
            
            if i[1]>0:
                cost += i[1]*self.customHeur[1]
            elif i[1]<0:
                cost += abs(i[1]*self.customHeur[3])
            
            costs.append(cost)
            
        return np.array(costs)
            
                
  
            
    def updatePossMoves(self, possMovsValid, costsOfPossMoves):
        
        #Frontier
        
        # self.currState.board[tuple(newPossMoves.T)] = np.arange(self.stepCount+1,self.stepCount+len(newPossMoves)+1,1)
        possMovsValid = possMovsValid.tolist()
        costsOfPossMoves = costsOfPossMoves.tolist()
        
        newPossMoves =[]
        newPossCosts = []
        j=0
        for i in possMovsValid:
            if i not in self.currState.possMoves:
                newPossMoves.append(i)
                newPossCosts.append(costsOfPossMoves[j])
            
            j+=1
        
        allPossMoves = self.currState.possMoves + newPossMoves
        allPossCosts = self.currState.possCosts + newPossCosts
        
        ordered = np.array(allPossCosts).argsort()
        
        self.currState.possMoves = [allPossMoves[i] for i in ordered]
        self.currState.possCosts =  [allPossCosts[i] for i in ordered]
    
                
        
                
    def getNextMoveL(self):
        
        allPossMoves = self.currState.possMoves
        nextLoc = allPossMoves[0]
        self.currState.pathCost = self.currState.possCosts[0]
        
        self.currState.possCosts = self.currState.possCosts[1:]
        self.currState.possMoves = self.currState.possMoves[1:]
        # print('cost at next move ', self.currState.pathCost)
        # self.currState.possMoves = allPossMoves[np.all(allPossMoves != nextLoc, axis =1),:]
        return nextLoc
    
    def updateBoard(self, newPossMoves):
        
        if len(newPossMoves):
            newPossMoves = np.array(newPossMoves)
            self.currState.boardObj.board[tuple(newPossMoves.T)] = np.arange(self.stepCount+1,self.stepCount+len(newPossMoves)+1,1)
            self.stepCount = self.stepCount+len(newPossMoves)
    
        
    ######                    
                
    [possMovsValid, costsOfPossMoves] = AppSeq(self) #branches
    updatePossMoves(self, possMovsValid, costsOfPossMoves)
    updateBoard(self, possMovsValid)
    # print('all curr poss locs \n', self.currState.possMoves)
    nextLoc = getNextMoveL(self)
    # print('next loc is ',nextLoc)
    return nextLoc   