"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import choice
lista = [0, 1, 2, 3, 4, 5]
n = choice(lista)
x = int(input('Em que número eu pensei?'))
if x == n:
    print('\033[7;30mVocê venceu!CARALHO!\033[m')
else:
    print('SE FUDEU!!!')
