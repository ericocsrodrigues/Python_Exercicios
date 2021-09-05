"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
atual = date.today().year
maior_idade = menor_idade = 0
for n in range(7):
    ano = int(input('Informe o ano de nascimento: '))
    idade = atual - ano
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print(f'De todos digitados temos \033[34m{maior_idade}\033[m maiores de idade e \033[31m{menor_idade}\033[m menores idedade')
