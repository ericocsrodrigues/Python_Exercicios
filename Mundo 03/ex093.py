"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

from time import sleep
from BibliotecaCm7.menu import menu, lin
menu(' JOGADOR ')
jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(partidas):
    gol.append(int(input(f'Quantos gols na {i + 1}ª partida: ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
lin()
print(jogador)
lin()
for i, v in jogador.items():
    print(f' - O campo {i} tem valor {v} ')
lin()
print(f'O jgoador {jogador["nome"]} jogou {partidas} partidas:')
for i, v in enumerate(gol):
    print(f'   => Na {i + 1}ª partiga marcou {v} gols.')
    sleep(0.5)
print(f'   => Foi um total de {jogador["total"]}')
