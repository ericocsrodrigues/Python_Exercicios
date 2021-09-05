"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

cont = 0
soma = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Informe um número: '))
    soma += n
    cont += 1
    print('-' * 20)
    continuar = str(input('Continuar [S/N]: ')).upper().strip()[0]
    print('-' * 20)
media = soma / cont
print(f'Foram digitados {cont} número e a média entre eles é {media}')
print(f'FIM! ')
