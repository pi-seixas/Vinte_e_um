# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:55:57 2019

@author: pisei
"""

import os
import random

baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def dar_as_cartas(baralho):
    mao = []
    for i in range(2):
        random.shuffle(baralho)
        carta = baralho.pop()
        if carta == 11:carta = "J"
        if carta == 12:carta = "Q"
        if carta == 13:carta = "K"
        if carta == 14:carta = "A"
        mao.append(carta)
    return mao