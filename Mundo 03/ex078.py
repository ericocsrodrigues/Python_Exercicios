'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

lista = list()
for x in range(5):
    lista.append(int(input(f'Digite um valor para a posição {x}: ')))
print(f'O maior valor foi o {max(lista)} e está na posição: ', end='')
for c, v in enumerate(lista):
    if v == max(lista):
        print(f'{c}...', end='')
print()
print(f'O menor valor foi o {min(lista)} e está na posição: ', end='')
for c, v in enumerate(lista):
    if v == min(lista):
        print(f'{c}...', end='')