"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista = list()
while True:
    v = int(input(f'Digite um valor: '))
    if v not in lista:
        lista.append(v)
        print('Valor adicionado...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Continuar[S/N]: ')).strip()[0]
    if cont in 'Nn':
        break
lista.sort()
print(f'A lista ficou: {lista}')


