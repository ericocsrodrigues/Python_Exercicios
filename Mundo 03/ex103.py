"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente.
"""
from BibliotecaCm7.menu import menu, lin


def ficha(n='<FULADO>', g=0):
    """
    -> Mostra a ficha de um jogador
    :param n: Nome do jogador
    :param g: Número de gols no campeonato
    :return: Ficha contendo nome e número de gols de um jogador
    """
    print(f'O jogador {n} marcou {g} gols no campeonato')


menu('Ficha Jogador')
nome = str(input('Nome do jogador: ')).strip().title()
gols = str(input('Número de gols: '))
lin()
if gols.isalnum():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(g=gols)
else:
    ficha(nome, gols)

