#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:15:23 2022

@author: dharmendrakhakhar
"""

import board
import numpy as np
class boardStates(board.board):
    
    def __init__ (self, parent, nextLoc, possMoves = [], possCosts = [], pathCost =np.empty((0,2), dtype = 'int')):
        self.currLoc = nextLoc
        self.prevLoc = parent.currLoc
        self.board = parent.board
        self.possMoves = possMoves
        self.possCosts = possCosts
        
        self.pathCost = pathCost
        # self.costsOfPossMoves = np.empty((0,4), dtype = 'int')
        
    def goalStateTest(self):
        if (self.board[self.currLoc] == -2):
            return True
        else:
            return False
        
    def isBanned(self, potLoc):
        nppotLoc = np.array(potLoc)
        print('is banned', [self.board[tuple(nppotLoc.T)]==-1])
        return nppotLoc[self.board[tuple(nppotLoc.T)]==0,:] #np array