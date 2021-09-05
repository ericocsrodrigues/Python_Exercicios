"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from BibliotecaCm7.menu import menu
from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
partida = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
menu(' JODO DE DADOS ')
for i, v in partida.items():
    print(f' -{i} tirou {v} no dado')
    sleep(1)
ranking = sorted(partida.items(), key=itemgetter(1), reverse=True)
menu(' RANKING ')
for i, v in enumerate(ranking):
    print(f' - {i + 1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
