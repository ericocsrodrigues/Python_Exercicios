"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opões:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔÔÔ')
print('\033[1;35m-=-\033[m' * 10)
print(f'Computador jogou: \033[4;31m{itens[pc]}\033[m')
print(f'Jogador jogou: \033[4;34m{itens[jogador]}\033[m')
print('\033[1;35m-=-\033[m' * 10)
if pc == 0:
    if jogador == 0:
        print('\033[0;32mEMPATE\033[m')
    elif jogador == 1:
        print('\033[4;34mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[4;31mCOMPUTADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')
elif pc == 1:
    if jogador == 0:
        print('\033[4;31mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[0;32mEMPATE\033[m')
    elif jogador == 2:
        print('\033[4;34mJOGADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')
elif pc == 2:
    if jogador == 0:
        print('\033[4;34mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[4;31mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[0;32mEMPATE\033[m')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')
