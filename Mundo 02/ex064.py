"""
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
"""
print('\033[32m~\033[m' * 32)
print('\033[31m999 para interromper o programa.\033[m')
print('\033[32m~\033[m' * 32)
soma = cont = 0
c = int(input('Digite um número: '))
while c != 999:
    soma += c
    cont += 1
    c = int(input('Digite um número: '))
print(f'Foram digitados {cont} números e a soma deles é {soma}')
