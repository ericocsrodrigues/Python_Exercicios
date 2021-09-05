"""
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto
"""

ano = int(input('Informe o ano para análise: '))
if ano % 4 == 0:
    print(f'O ano {ano} é \033[4;31mBISSEXTO\033[m')
else:
    print(f'O ano {ano} \033[7;30mNÃO\033[m é \033[4;34mBISSEXTO\033[m')