"""
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

r = float(input('Quanto dinheiro você tem na carteira? R$'))
d = r / 3.27
print(f'Com esse valor \033[1;34mR${r:.2f}\033[m você pode comprar \033[4;36m${d:.2f}\033[m')
