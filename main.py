#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:04:45 2022

@author: dharmendrakhakhar
"""
from Player._Player import Player
import board as bd

import numpy as np
# P1 = Player(bd.board())
# P1.action('BFS')

# P2 = Player(bd.board())
# P2.action('DFS')


# h = np.array([2,1,2,3]) # 2 and 3 are same but left-first convention
# P3 = Player(bd.board(), customHeur = h)
# P3.action('UCS')

# h = np.array([2,1,2,3]) # 2 and 3 are same but left-first convention
# P4 = Player(bd.board(), customHeur = h)
# P4.action('GBFS')

# h = np.array([2,1,2,3]) # 2 and 3 are same but left-first convention
# P5 = Player(bd.board(), customHeur = h)
# P5.action('Astar')

P6 = Player(bd.board((5,4), blocks = np.array([[1,2,3],[2,2,1]]), start = [3,2],end = [2,1]))
P6.action('BFS')


P7 = Player(bd.board((5,4), blocks = np.array([[1,2,3],[2,2,1]]), start = [3,2],end = [2,1]))
P7.action('DFS')

h = np.array([2,3,2,1]) # 2 and 3 are same but left-first convention

P8 = Player(bd.board((5,4), blocks = np.array([[1,2,3],[2,2,1]]), start = [3,2],end = [2,1]), customHeur = h)
P8.action('UCS')

h = np.array([2,3,2,1]) # 2 and 3 are same but left-first convention

P9 = Player(bd.board((5,4), blocks = np.array([[1,2,3],[2,2,1]]), start = [3,2],end = [2,1]), customHeur = h)
P9.action('GBFS')

h = np.array([2,3,2,1]) # 2 and 3 are same but left-first convention

P10 = Player(bd.board((5,4), blocks = np.array([[1,2,3],[2,2,1]]), start = [3,2],end = [2,1]), customHeur = h)
P10.action('Astar')