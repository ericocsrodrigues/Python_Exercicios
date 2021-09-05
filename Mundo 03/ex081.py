"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = list()
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Continuar[S/N]: ')).strip()[0]
    if escolha in 'Nn':
        break
print('-=-' * 20)
print(f'Foram digitados {cont} valores')
lista2 = lista[:]
lista2.sort(reverse=True)
print(f'A lista ordenada e de trás para frente fica: {lista2}')
if 5 in lista:
    for c, v in enumerate(lista):
        if 5 == v:
            print(f'O valor 5 foi digitado e está na posição {c}')
else:
    print(f'O 5 não foi digitado! ')
