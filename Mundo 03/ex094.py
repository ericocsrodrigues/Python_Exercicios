"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

from BibliotecaCm7.cores import cor
from BibliotecaCm7.menu import menu, lin

menu('Cadastro')

pessoas = {}
listagem = []
cont = soma_idade = 0
escolha = ' '
while True:
    pessoas['nome'] = str(input('Nome: ')).strip().title()
    sexo = str(input(f'Sexo [M/F]: ')).strip()[0].upper()
    while sexo not in 'FfMm':
        print(f'{cor("vermelho")}Valor inválido!{cor("zerar")} Digite apenas {cor("azul")}[M/F]{cor("zerar")}')
        sexo = str(input(f'Sexo [M/F]: ')).strip()[0].upper()
    pessoas['sexo'] = sexo
    pessoas['idade'] = int(input('Idade: '))
    cont += 1
    soma_idade += pessoas['idade']
    listagem.append(pessoas.copy())
    pessoas.clear()
    x = str(input('CONTINUAR [S/N]: ')).strip()[0]
    while x not in 'SsNn':
        print(f'{cor("negro")}Valor inválido!{cor("zerar")} Digite apenas {cor("azul")}[S/N]{cor("zerar")}')
        x = str(input('CONTINUAR [S/N]: ')).strip()[0]
    escolha = x
    if escolha in 'Nn':
        break
media_idade = soma_idade / cont
lin()
print(f'No total foram cadastrados {cont} pessoas.')
lin()
print(f'A média das idades é {media_idade} anos')
lin()
print('A listagem de mulher cadastradas é:', end=' ')
for i, v in enumerate(listagem):
    if listagem[i]['sexo'] == 'F':
        print(f"{listagem[i]['nome']}", end=' ')
print('')
lin()
print('A listagem de pessoas com idade acimada média é:', end=' ')
for i, v in enumerate(listagem):
    if listagem[i]['idade'] > media_idade:
        print(f'{listagem[i]["nome"]}', end=' ')
print()
print(listagem)

