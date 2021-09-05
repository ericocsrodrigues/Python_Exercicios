"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
\033[0;31m[ 1 ] - Converter para BINÁRIO\033[m
\033[0;33m[ 2 ] - Converter para OCTAL\033[m
\033[0;34m[ 3 ] - Converter para HEXADECIMAL:
''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igal a {hex(num)[2:]}')
else:
    print('\033[7;30mOpção inválida! Tente novamente.\033[m')


























