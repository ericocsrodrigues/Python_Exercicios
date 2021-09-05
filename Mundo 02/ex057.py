"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Dados Inválidos. Tente novamente', end=' ')
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
if sexo in 'Mm':
    print('\033[34m')
elif sexo in 'Ff':
    print('\033[31m')
print(f'Sexo {sexo}, registrado com sucesso!')
