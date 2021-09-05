"""
Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

n = int(input('Digite um número: '))
print(f'O dobro de \033[1;31m{n}\033[m é: \033[7;30m{n * 2}\033[m')
print(f'O triplo de \033[1;33m{n}\033[m é: \033[7;30m{n * 3}\033[m')
print(f'A raiz quadrada de \033[1;34m{n}\033[m é: \033[7;30m{n ** 0.5:.2f}\033[m')
