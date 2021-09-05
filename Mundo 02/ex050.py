"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

cont = soma = 0
for _ in range(6):
    x = int(input('Infome um número: '))
    if x % 2 == 0:
        cont += 1
        soma += x
print(f'Dos 6 números digitados {cont} são pares e a soma deles é {soma}')
