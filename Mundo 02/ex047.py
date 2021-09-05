"""
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

'''for x in range(2, 51, 2):
    print(x, end=' ')
'''

print('-' * 30)
for n in range(1,6):
    var = int(input(f'{"Diga um número: ":>30}'))
    if var < 0:
        print(f'{"Apenas número positivo !!":>30"}')
        break
    if var % 2 == 0:
        print(f'\033[31m{var:>20}\033[m é Par !')
    else:
        print(f'\033[34m{var:>20}\033[m é Ímpar !')

print('*Fim* !')