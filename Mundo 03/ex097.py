"""
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’) Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
"""


def texto(x):
    t = len(x) + 4
    print('-' * t)
    print(f'  {x}')
    print('-' * t)


texto('Curso em vídeo')
