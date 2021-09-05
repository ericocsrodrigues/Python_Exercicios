"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares
"""

n = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))
print(f'Os valores digitados são: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na posição {n.index(3) + 1}')
else:
    print(f'O número 3 não foi digitado.')
print(f'Os valores pares são: ', end='')
for x in n:
    if x % 2 == 0:
        print(f'{x}', end=' ')
