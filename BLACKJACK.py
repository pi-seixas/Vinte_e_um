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

def total(mao):
    total = 0
    for carta in mao:
        if carta == "J" or carta == "Q" or carta == "K":
            total+= 10
        elif carta == "A":
            if mao[0] >= 11: 
                total += 1 
            else:
                total+= 11
        else:
            total+= carta
            
    return total

def jogar_de_novo():
    de_novo = input("você quer jogar de novo? (S/N) : ")
    if de_novo == "s":
        dealer_mao = []
        jogador_mao = []
        baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        jogando = True
    else:
        print ("Até a próxima!")
        jogando = False
    return jogando, dealer_mao, jogador_mao, baralho