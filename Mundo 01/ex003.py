"""
Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.
"""

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print(f'A some de \033[4;31m{n1}\033[m e \033[4;32m{n2}\033[m é: \033[7;30m{soma}\033[m')