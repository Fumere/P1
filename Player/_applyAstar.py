
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 22:23:51 2022

@author: dharmendrakhakhar
"""


import numpy as np

def applyAstar(self):
    
    
    
    def AppSeq(self):
        
        currLoc = self.currState.currLoc
        # print('curr loc is ',currLoc)
        possMovsMaybe = self.heur + np.array(currLoc)
        
        possMovsMaybeTruth = np.logical_and((possMovsMaybe>-1).all(axis=1), (possMovsMaybe<len(self.currState.boardObj.board)).all(axis=1))

        # print('maybe moves 1 ', possMovsMaybe[possMovsMaybeTruth,:])
        possMovsValidTruth = self.currState.isBanned(possMovsMaybe)
        
        totalTruth = np.logical_and(possMovsMaybeTruth , possMovsValidTruth)
        
        costsOfPossMovesGreedy = getGBFSCost(self, possMovsMaybe)
        
        costsOfPossMoves = costsOfPossMovesGreedy + self.customHeur + self.currState.pathCost
        
        possMovsValid = possMovsMaybe[totalTruth,:]
        costsOfPossMoves = costsOfPossMoves [totalTruth ]
        
        # print('valid moves', possMovsValid)
        # print('costs of moves', costsOfPossMoves)
        
        return [possMovsValid, costsOfPossMoves]
    
    def getGBFSCost(self, possMovsMaybe):
        
        dist = self.currState.boardObj.endLoc - np.array(possMovsMaybe)
        costs = []
        
        for i in range(np.size(possMovsMaybe, axis =0)):
            cost = 0
            if dist[i][0]>0:
                cost +=abs( dist[i][0]*self.customHeur[2])
            elif dist[i][0]<0:
                cost += abs(dist[i][0]*self.customHeur[0])
            
            if dist[i][1]>0:
                cost += abs(dist[i][1]*self.customHeur[1])
            elif dist[i][1]<0:
                cost += abs(dist[i][1]*self.customHeur[3])
            
            costs.append(cost)
            
        return np.array(costs)
            
                
  
            
    def updatePossMoves(self, possMovsValid, costsOfPossMoves):
        
        
        
        #Frontier
        
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
        
        # print('\n new moves ', newPossMoves)
        # print('\n new costs ', newPossCosts)
        # print('\n all costs ', self.currState.possCosts)
        # print('\n all moves ', self.currState.possMoves)
    
                
        
                
    def getNextMoveL(self):
        
        
        allPossMoves = self.currState.possMoves
        nextLoc = allPossMoves[0]
        ##IMPORTANT##
        ##Subtract GBFS cost counted until now to queue next moves. 
        ##Only UCS costs add up as path travelled + next move
        
        GBFScost = getGBFSCost(self, [nextLoc])

        self.currState.pathCost = self.currState.possCosts[0] - GBFScost
        
        self.currState.possCosts = self.currState.possCosts[1:]
        self.currState.possMoves = self.currState.possMoves[1:]
        # print('cost at next move ', self.currState.pathCost)
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