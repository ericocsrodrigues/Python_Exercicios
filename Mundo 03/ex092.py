"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from BibliotecaCm7.menu import menu
menu(' I N S S ')
from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: ')).strip().title()
trabalhador['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho [0 - não tem]: '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = ((trabalhador['contratação'] + 35) - datetime.now().year) + trabalhador['idade']
menu(' D A D O S ')
for i, v in trabalhador.items():
    print(f' - {i} tem valor {v}')
