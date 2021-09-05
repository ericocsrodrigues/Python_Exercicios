"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from os import system
from time import sleep
menu = 'MENU INICIAL'
menu2 = 'MENU OPÇÕES'
escolha = 0
while escolha != 5:
    system('cls')
    print('=' * 30)
    print(f'{menu:^30}')
    print('=' * 30)
    n1 = int(input('1º valor: '))
    n2 = int(input('2º valor: '))
    print('=' * 30)
    print(f'{menu2:^30}')
    print('=' * 30)
    print('''Escolha uma operação
    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos número
    [ 5 ] - Sair do programa''')
    print('=' * 30)
    escolha = int(input('Opção: '))
    if escolha == 1:
        soma = n1 + n2
        print(f'Soma = {soma}')
    elif escolha == 2:
        mult = n1 * n2
        print(f'Multiplicação: {mult}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior é : {n1}')
        if n2 > n1:
            print(f'O maior é: {n2}')
        else:
            print('Número são iguais')
    elif escolha == 4:
        print('Voltando para o menu inicial')
    sleep(1)
print('Fim da execução.')
sleep(2)
