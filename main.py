#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:04:45 2022

@author: dharmendrakhakhar
"""
from Player._Player import Player
# P = Player()
# P.action()

# P1 = Player()
# P1.action('DFS')


h = [2,1,3,4] # 2 and 3 are same but left-first convention
P2 = Player(customHeur=[2,1,3,4])
P2.action('UCS')
