"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint
print('\033[36m=-=\033[m' * 10)
print('   \033[34mVAMOS JOGAR PAR OU ÍMPAR')
print('\033[36m=-=\033[m' * 10)
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    par_impar = str(input('Par ou Ímpar [P/I]: ')).strip()[0]
    computador = randint(1, 10)
    soma = jogador + computador
    if soma % 2 ==0 and par_impar in 'Pp':
        print(f'O computador escolheu {computador} e o resultado foi {soma}. Você venceu!')
        print('Vamos jogar novamente')
        cont += 1
    elif soma % 2 == 1 and par_impar in 'Ii':
        print(f'O computador escolheu {computador} e o resultado foi {soma}. Você venceu!')
        print('Vamos jogar novamente')
        cont += 1
    else:
        print(f'')
        print(f'O computador escolheu {computador} e o resultado foi {soma}. Você perdeu!')
        break
print(f'Você venceu {cont} vezes.')
