"""
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma = cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        cont += 1
        soma += x
print(f'A soma dos {cont} valores é {soma}')
