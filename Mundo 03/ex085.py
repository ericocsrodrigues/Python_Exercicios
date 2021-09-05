"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""

lista = [[], []]
for _ in range(1, 8):
    x = int(input(f'Digite um valor {_}ª: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)
lista[0].sort()
lista[1].sort()
print('-=' * 30)
print(f'Todos os valores são: {lista}')
print(f'Os valores pares são: {lista[0]}')
print(f'Os valores ímpares são: {lista[1]}')

