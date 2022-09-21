#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:03:00 2022

@author: dharmendrakhakhar
"""
import boardStates as bds
import board as bd
import numpy as np
from Player._applyBFS import applyBFS
class Player():
    
    def __init__ (self, aboard = bd.board(), h = np.array([[-1,0,1,0],[0,1,0,-1]]).T,c=0):
        
        self.currState = bds.boardStates(aboard, aboard.currLoc)
        self.heur = h
        self.stepCount = c
        

    def action (self,  method = 'BFS'):
        
        while (self.currState.goalStateTest):

            nextLoc = applyBFS(self)
            # print('next loc is ',nextLoc)
            self.currState = bds.boardStates(self.currState, nextLoc, self.currState.possMoves)








