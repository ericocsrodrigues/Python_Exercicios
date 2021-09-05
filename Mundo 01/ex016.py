"""
Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""

from math import trunc
x = float(input('Informe um número: '))
print(f'O valor digitado é \033[1;31m{x}\033[m e a sua porção inteira é \033[4;34m{trunc(x)}\033[m')
