"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""

n = int(input('Escolha um número para ver o seu fatorial: '))
x = n
f = 1
while x > 0:
    print(f'\033[34m{x}\033[m', end='')
    print('\033[31m x \033[m' if x > 1 else ' \033[32m=\033[m ', end='')
    f *= x
    x -= 1
print(f'\033[34m{f}\033[m')
