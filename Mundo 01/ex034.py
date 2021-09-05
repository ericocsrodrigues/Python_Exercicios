"""
Exercício Python 34: Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento. Para salários superiores a
R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento
é de 15%
"""
x = '-*-*' * 10
print(f'\033[0;34m{x}\033[m')
s = float(input('Informe o salário: R$'))
if s > 1250:
    s *= 1.1
    print(f'R${s:.2f}')
else:
    s *= 1.15
    print(f'Novo salário: R${s:.2f}')
