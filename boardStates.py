#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:15:23 2022

@author: dharmendrakhakhar
"""

from board import board
import numpy as np
class boardStates(board):
    
    def __init__ (self, parent, nextLoc, possMoves = [], possCosts = [], pathCost = int()):
        self.currLoc = nextLoc
        self.boardObj = parent
        # self.board = parent.board
        self.possMoves = possMoves
        self.possCosts = possCosts
        
        self.pathCost = pathCost
        # self.costsOfPossMoves = np.empty((0,4), dtype = 'int')
        
        # print('\n ------------ \n', 'new state to enter \n ', nextLoc,'\n current board rotated \n', np.srot90(parent.board,1), '\n current board \n', parent.board)
        # print('\n possible costs \n', [(x+self.pathCost) for x in possCosts], )
        
        
    def goalStateTest(self):
        if (len(self.possMoves) == 0):
            print('exhausted all moves \n')
            print('final board: \n', np.rot90(self.boardObj.board,1))
            return False
        else:
            return True
        
    def isBanned(self, potLoc):
        
        isNotBanned = []
        j=0
        nppotLoc = np.array(potLoc)
        
        possMovsMaybeTruth = np.logical_and((potLoc>-1).all(axis=1), (potLoc<len(self.boardObj.board)).all(axis=1))
        for i in possMovsMaybeTruth:
            if i:
                isNotBanned.append((self.boardObj.board[tuple(nppotLoc[j,:])]==0).tolist())
            else:
                isNotBanned.append(False)
            
            j+=1
        # print('is banned', isNotBanned)
        return  isNotBanned#np array