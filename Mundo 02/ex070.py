"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

print('\033[36m-\033[m' * 20)
print(f'\033[33m{"BARATÃO PYTHON":•^20}')
print('\033[36m-\033[m' * 20)
maisbarato = ' '
precobarato = 10000
totalcompra = 0
produto1000 = 0
while True:
    produto = str(input('Nome poduto: ')).strip()
    valor = float(input('Valor produto: R$ '))
    totalcompra += valor
    if valor < precobarato:
        maisbarato = produto
        precobarato = valor
    if valor > 100:
        produto1000 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Continuar [S/N]: ')).upper().strip()[0]
    if escolha in 'N':
        break
print(f'Total gasto: R${totalcompra:.2f}')
print(f'{produto1000:.2f} custaram abaixo de R$1000,00')
print(f'O produto mais barato é {maisbarato.title()} e custou R${precobarato:.2f}')
print(f'{"FIM DO PROGRAMA":-^40}')
