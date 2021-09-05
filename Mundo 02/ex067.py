"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

print('\033[36m▼\033[m' * 15)
print('       TABUADA')
print('\033[36m▲\033[m' * 15)
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    for x in range(1, 11):
        print(f'{n} x {x:2} = {(n * x):2}')
    sair = str(input('Continuar [S/N]: ')).strip()[0]
    if sair in 'Nn':
        break
