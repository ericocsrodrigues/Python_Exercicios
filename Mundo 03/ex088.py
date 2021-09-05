"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
apostas = list()
dados = list()
jogos = int(input('Quantos jogos serão gerados? '))
for n in range(jogos):
    for y in range(6):
        dados.append(randint(1, 60))
    dados.sort()
    apostas.append(dados[:])
    dados.clear()
print('\033[31m-=\033[m' * 15)
for i, j in enumerate(apostas):
    print(f'Jogo {i+1}: {j}')
print('\033[34m-=\033[m' * 15)
