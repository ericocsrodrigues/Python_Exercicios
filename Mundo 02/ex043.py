"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""

altura = float(input('Informe a altura em METROS: '))
peso = float(input('Informe o peso: '))
imc = peso / altura ** 2
if 0 < imc <= 18.5:
    print('Abaixo do peso.')
elif 18.5 < imc <= 25:
    print('Peso ideal.')
elif 25 < imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
elif 40 < imc < 50:
    print('Obesidade Mórbida.')
else:
    print('Algum dado informa errado. Tente novamente!')
