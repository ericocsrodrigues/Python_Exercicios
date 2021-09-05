"""
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""
print('=' * 20)
print('[999] - Para sair.')
print('=' * 20)
cont = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        soma += n
        cont += 1
print(f'Foram digitados {cont} números e a soma de todos é {soma}')
