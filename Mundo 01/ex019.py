"""
Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

from random import choice, a
n1 = str(input('1º aluno: '))
n2 = str(input('2º aluno: '))
n3 = str(input('3º aluno: '))
n4 = str(input('4º aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
escolhido2 = choice(lista)
print(f'O aluno escolhido foi \033[4;34m{escolhido}\033[m')
