"""
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""

n = str(input('Informe seu nome completo: ')).strip()
nome = n.split()
print(nome)
print(n)
print(f'Seu primeiro nome é: \033[1;34m{nome[0]}\033[m \nSeu último nome é: \033[7;30m{nome[len(nome) - 1]}\033[m')
print()
