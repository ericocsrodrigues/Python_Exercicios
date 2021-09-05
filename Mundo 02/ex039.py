"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
atual = date.today().year
ano = int(input('Informe seu ano de nascimento: '))
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
if idade == 18:
    print('\033[1;31mEstá na hora de se alistar!\033[m')
elif idade < 18:
    print(f'Ainda não está na hora de se alistar. Está faltando \033[4;34m{18 - idade} anos\033[m.')
elif idade > 18:
    print(f'Já passou da hora de se alistar. Você está \033[4;34m{idade -18} anos\033[m atrasado!')
