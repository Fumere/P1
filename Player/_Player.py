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
from Player._applyGBFS import applyGBFS
from Player._applyAstar import applyAstar


class Player():
    
    def __init__ (self, aboard = bd.board(), c=0, customHeur=[] ):  #h = np.array([[-1,0,1,0],[0,1,0,-1]]).T,
        
        self.currState = bds.boardStates(aboard, aboard.currLoc)
        self.heur = np.array([[-1,0,1,0],[0,1,0,-1]]).T
        self.stepCount = c
        
        self.customHeur = customHeur
        

    def action (self,  method = 'BFS'):
        
        goalStateTest = True
        if (method == 'BFS'):
            print('\n -----method BFS----- \n')
            while (goalStateTest):
                
                
                nextLoc = applyBFS(self)
                # print('next loc is ',nextLoc)
                self.currState = bds.boardStates(self.currState.boardObj, nextLoc, self.currState.possMoves)
                goalStateTest = self.currState.goalStateTest()
                
        elif (method == 'DFS'):
            print('\n -----method DFS----- \n')
            while (goalStateTest):
                
                
                nextLoc = applyDFS(self)
                # print('next loc is ',nextLoc)
                self.currState = bds.boardStates(self.currState.boardObj, nextLoc, self.currState.possMoves)
                goalStateTest = self.currState.goalStateTest()
                
        elif (method == 'UCS'):
            print('\n -----method UCS----- \n')
            while (goalStateTest):
                
                
                nextLoc = applyUCS(self)
                # print('next loc is ',nextLoc)
                self.currState = bds.boardStates(self.currState.boardObj, nextLoc, self.currState.possMoves, self.currState.possCosts, self.currState.pathCost)                
                goalStateTest = self.currState.goalStateTest()
                
        elif (method == 'GBFS'):
            print('\n -----method GBFS----- \n')
            while (goalStateTest):
                
                
                nextLoc = applyGBFS(self)
                # print('next loc is ',nextLoc)
                self.currState = bds.boardStates(self.currState.boardObj, nextLoc, self.currState.possMoves, self.currState.possCosts, self.currState.pathCost)                
                goalStateTest = self.currState.goalStateTest()
                
        elif (method == 'Astar'):
            print('\n -----method Astar----- \n')
            while (goalStateTest):
                
                
                nextLoc = applyAstar(self)
                # print('next loc is ',nextLoc)
                self.currState = bds.boardStates(self.currState.boardObj, nextLoc, self.currState.possMoves, self.currState.possCosts, self.currState.pathCost)                
                goalStateTest = self.currState.goalStateTest()





