"""
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

p = float(input('Qual o preço do produto? R$'))
d = p * 0.95
print(f'O produto que custava \033[4;30mR${p:.2f}\033[m com desconto de 5% vai sair por \033[1;36mR${d:.2f}\033[m')
