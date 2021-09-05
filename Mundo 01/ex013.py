"""
Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

sal = float(input('Qual é o salário de um funcionário? R$'))
print(f'O funcionário que recebia \033[1;31mR${sal:.2f}\033[m com o aumento de 15% vai passar a receber \033[4;34mR${sal * 1.15:.2f}\033[m')
