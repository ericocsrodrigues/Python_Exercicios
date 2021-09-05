"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'\033[31mEu sortiei os valores \033[34m{n}\n')
print(f'Os valores sorteados são: ', end='')
for x in n:
    print(f'{x}', end=' ')
print(f'\nO maior valor é {max(n)}')
print(f'O menor valor é {min(n)}')