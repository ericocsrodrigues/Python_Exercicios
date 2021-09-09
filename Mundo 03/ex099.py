"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep
from BibliotecaCm7.menu import menu, lin


def maior(*num):
    print(f'Analisando os valores informados...')
    sleep(1.5)
    for x in num:
        print(f'{x}', end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores.')
    print(f'O maior número informado foi: {max(num)}')


maior(1, 2, 4, 76, 13)


