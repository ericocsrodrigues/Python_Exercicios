"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

listagem = list()
dados = list()
pesados = list()
leves = list()
cont = 0
pesado = 0
leve = 0
while True:
    dados.append(str(input('Nome:')).strip())
    dados.append(int(input('Peso: ')))
    listagem.append(dados[:])
    cont += 1
    dados.clear()
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Continuar [S/N]: ')).strip()[0]
    if escolha in 'Nn':
        break
print('=' * 40)
print(f'Foram cadastrado {cont} pessoas:')
for p in listagem:
    print(f'{p[0].title()} com {p[1]:.2f}kg')
print('=' * 40)
for p in listagem:
    if p == listagem[0]:
        pesado = p[1]
        pesados.append(p[0])
    else:
        if p[1] == pesado:
            pesados.append(p[0])
        elif p[1] > pesado:
            pesado = p[1]
            pesados.clear()
            pesados.append(p[0])
print(f'O maior peso é {pesado}. E são: {pesados}')
print('=' * 40)
for p in listagem:
    if p == listagem[0]:
        leve = p[1]
        leves.append(p[0])
    else:
        if p[1] == leve:
            leves.append(p[0])
        elif p[1] < leve:
            leve = p[1]
            leves.clear()
            leves.append(p[0])
print(f'O menor peso é {leve}. E são: {leves}')