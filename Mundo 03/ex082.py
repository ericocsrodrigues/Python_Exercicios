"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Continuar[S/N]: ')).strip()[0]
    if escolha in 'Nn':
        break
lista.sort()
listapar = list()
listaimpar = list()
for x in lista:
    if x % 2 == 0:
        listapar.append(x)
    else:
        listaimpar.append(x)
print(f'Os números digitados são: \033[34m{lista}\033[m')
print(f'Os número pares são: \033[32m{listapar}\033[m')
print(f'Os números ímpares são: \033[33m{listaimpar}\033[m')

