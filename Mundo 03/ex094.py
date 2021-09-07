"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

from BibliotecaCm7.cores import cor
pessoas = {}
listagem = []
opção = ' '
while True:
    pessoas['nome'] = str(input('Nome: ')).strip().title()
    sexo = str(input(f'Sexo {cor("vermelho")}[M/F]: ')).strip()[0]
    if sexo not in 'FfMm':
        print(f'{cor("vermelho")}Valor inválido!{cor("zerar")} Digite apenas \033[M/F]')
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip()[0]

