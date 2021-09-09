"""

"""
from BibliotecaCm7.menu import menu, lin


def ficha(n='<FULADO>', g=0):
    """
    -> Mostra a ficha de um jogador
    :param n: Nome do jogador
    :param g: Número de gols no campeonato
    :return: Ficha contendo nome e número de gols de um jogador
    """
    return f'O jogador {n} marcou {g} gols no campeonato'


menu('Ficha Jogador')
nome = str(input('Nome do jogador: ')).strip().title()
gols = (input('Número de gols: '))
lin()
print(ficha(nome, gols))
