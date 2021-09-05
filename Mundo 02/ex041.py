"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""

from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de nascimento do atleta: '))
idade = atual - nasc
if 0 < idade <= 9:
    print(f'Com idade de {idade} anos.\nCategoria: \033[0;32mMIRIM\033[m')
elif 9 < idade <= 14:
    print(f'Com idade de {idade} anos.\nCategoria: \033[0;33mINFANTIL\033[m')
elif 14 < idade <= 19:
    print(f'Com idade de {idade} anos.\nCategoria: \033[0;35mJUNIOR\033[m')
elif 19 < idade <= 25:
    print(f'Com idade de {idade} anos.\nCategoria: \033[0;31mSÊNIOR\033[m')
elif 100 > idade > 25:
    print(f'Com idade de {idade} anos.\nCategoria: \033[0;34mMASTER\033[m')
else:
    print(f'Ano de nascimento inválido')
