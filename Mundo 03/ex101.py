"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
nas eleições.
"""
from BibliotecaCm7.menu import menu,lin
from datetime import datetime


def voto(x):
    idade = datetime.now().year - x
    if 0 < idade < 18:
        return 'NEGADO'
    elif 18 < idade < 65:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'


menu('VOTO')
nasc = int(input('Informe seu ano de nascimento: '))
idade = datetime.now().year - nasc
print(f'Com {idade} o voto é {voto(nasc)}')
