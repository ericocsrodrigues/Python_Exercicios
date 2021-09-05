"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
peso = float(input('Informe o peso da 1ª pessoa: '))
maior = menor = peso
for x in range(2, 6):
    pes = float(input(f'Informe o peso da {x}ª pessoa: '))
    if pes > maior:
        maior = pes
    elif pes < menor:
        menor = pes
print(f'O maior peso informado foi {maior:.2f}kg e o menor foi {menor:.2f}kg')
