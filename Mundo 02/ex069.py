"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

print('\033[36m-\033[m' * 20)
print('\033[32mRealize o cadastro: ')
print('\033[36m-\033[m' * 20)
mais18 = 0
cont_homens = 0
mulher20 = 0
cont = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    cont += 1
    if sexo in 'Mm':
        cont_homens += 1
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    if idade > 18:
        mais18 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('CONTINUAR [S/N]: ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'\nForam cadastrador {cont} pessoas.')
print(f'{mais18} pessoas tem mais de 18 anos.')
print(f'Foram cadastrador {cont_homens} homens.')
print(f'{mulher20} mulheres tem menos de 20 anos.')
