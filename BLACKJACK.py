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

def hit(mao):
    carta = baralho.pop()
    if carta == 11:carta = "J"
    if carta == 12:carta = "Q"
    if carta == 13:carta = "K"
    if carta == 14:carta = "A"
    mao.append(carta)
    return mao
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def resultado(dealer_mao, jogador_mao):
    clear()
    print ("O dealer tem " + str(dealer_mao) + " com um total de " + str(total(dealer_mao)) + " pontos")
    print ("Você tem " + str(jogador_mao) + " com um total de " + str(total(jogador_mao)) + " pontos " )
    
def pontos(dealer_mao, jogador_mao):
    if total(jogador_mao) == 21:
        print(jogador_mao, dealer_mao)
        print ("Parabéns! você tirou 21!")
        return True
    elif total(dealer_mao) == 21:
        print(jogador_mao, dealer_mao)        
        print ("Você perdeu! O dealer tirou 21")
        return False
    elif total(jogador_mao) > 21:
        print(jogador_mao, dealer_mao)
        print ("Estourou! Você perdeu!")
        return False
    elif total(dealer_mao) > 21:
        print(jogador_mao, dealer_mao)               
        print ("O Dealer estourou! Você ganhou!")
        return True
    elif total(jogador_mao) < total(dealer_mao):
        print(jogador_mao, dealer_mao)
        print ("Você perdeu!")
        return False
    elif total(jogador_mao) > total(dealer_mao):               
        print(jogador_mao, dealer_mao)
        print ("Você ganhou!")
        return True
    if jogador_mao[0]=='A'==jogador_mao[1]:
        montante+=100
        print('Você ganhou $100 por tirar um duplo As')       
    if jogador_mao[0]==jogador_mao[1]==jogador_mao[2]==7:
        montante=montante*3
        print('Parabéns! você tirou um triplo 7 e triplicou o seu montante!')
        
def checa_blackjack(jogador_mao, montante, aposta):
    if total(jogador_mao)==21:
        montante+=aposta*1.5
        print('Você tem ${0}' .format(montante))
    else:
        montante+=aposta
        print('Você tem ${0}' .format(montante))
    return montante

def vinte_um(dealer_mao, jogador_mao):
    if total(jogador_mao) == 21:
        print ("Parabéns! você tirou 21!")
        jogar_de_novo()
    elif total(dealer_mao) == 21:        
        print ("Você perdeu! O dealer tirou 21")
        jogar_de_novo()
        
def jogo():
    n=int(input('Com quantos baralhos vc quer jogar? '))
    baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4*n
    escolha = 0
    clear()
    print ("VAMOS JOGAR BLACKJACK INSPER VERSION")
    montante=500
    dealer_mao = dar_as_cartas(baralho)
    jogador_mao = dar_as_cartas(baralho)
    jogando = True
    while jogando:
        print('Você tem ${0}' .format(montante))
        aposta=int(input('Quanto você quer apostar? '))
        aposta_valida = False
        while not aposta_valida:
            if montante < aposta:
                print('Você não tem dinheiro o suficiente pra isso')
                aposta=int(input('Quanto você quer apostar? '))
            else:
                aposta_valida = True
        print ("O dealer saiu com " + str(dealer_mao[0]))
        print ("Você começou com " + str(jogador_mao) + " com um total de " + str(total(jogador_mao)) + " pontos")
        vinte_um(dealer_mao, jogador_mao)
        escolha = input("O que você quer fazer? [H]it, [F]icar, or [S]air: ").lower()
        clear()
        if escolha == "h":
            hit(jogador_mao)
            while total(dealer_mao) < 18:
                hit(dealer_mao)
            venceu = pontos(dealer_mao, jogador_mao)
            if venceu:
                montante = checa_blackjack(jogador_mao, montante, aposta)
            jogando, dealer_mao, jogador_mao, baralho = jogar_de_novo()
        elif escolha == "f":
            while total(dealer_mao) < 18:
                hit(dealer_mao)
            venceu = pontos(dealer_mao, jogador_mao)
            if venceu:
                montante = checa_blackjack(jogador_mao, montante, aposta)
            jogando, dealer_mao, jogador_mao, baralho = jogar_de_novo()
        elif escolha == "s":
            print ("Até a próxima!")
            jogando = False


jogo()



