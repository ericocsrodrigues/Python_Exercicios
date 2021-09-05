"""
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

num = int(input('Digite um número: '))
cont = 0
for x in range(1, num + 1):
    if num % x == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{x}', end=' ')
if cont == 2:
    print('\nNÚMERO PRIMO!')
else:
    print('\nNÚMERO NÃO É PRIMO!')


