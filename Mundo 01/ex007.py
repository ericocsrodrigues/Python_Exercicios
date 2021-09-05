"""
Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota: '))
m = (n1 + n2) / 2
print(f'A média entre \033[1;34m{n1}\033[m e \033[1;33m{n2}\033[m é: \033[7;30m{m}\033[m')
