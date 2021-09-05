"""
Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

n = int(input('Digite um número: '))
print(f'O antessesor de \033[1;31m{n}\033[m é \033[1;32m{n - 1}\033[m e o sucessor é \033[7;30m{n + 1}\033[m')
