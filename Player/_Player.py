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
from Player._applyDFS import applyDFS
from Player._applyUCS import applyUCS

class Player():
    
    def __init__ (self, aboard = bd.board(), customHeur=[], c=0 ):  #h = np.array([[-1,0,1,0],[0,1,0,-1]]).T,
        
        self.currState = bds.boardStates(aboard, aboard.currLoc)
        self.heur = np.array([[-1,0,1,0],[0,1,0,-1]]).T
        self.stepCount = c
        
        self.customHeur = customHeur
        

    def action (self,  method = 'BFS'):
        
        if (method == 'BFS'):
            while (self.currState.goalStateTest):
                
                nextLoc = applyBFS(self)
                # print('next loc is ',nextLoc)
                self.currState = bds.boardStates(self.currState, nextLoc, self.currState.possMoves)

        elif (method == 'DFS'):
            
            while (self.currState.goalStateTest):
                
                nextLoc = applyDFS(self)
                # print('next loc is ',nextLoc)
                self.currState = bds.boardStates(self.currState, nextLoc, self.currState.possMoves)
                
        elif (method == 'UCS'):
            
            while (self.currState.goalStateTest):
                
                nextLoc = applyUCS(self)
                # print('next loc is ',nextLoc)
                self.currState = bds.boardStates(self.currState, nextLoc, self.currState.possMoves)                







