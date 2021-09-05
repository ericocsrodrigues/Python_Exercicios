"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 parta viagens mais longas.
"""

print("""\033[0;34mExercício Python 31: Desenvolva um programa que pergunte a distância de uma 
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 parta viagens mais longas.\033[m""")
km = float(input('\nInforme a distância da viagem em km: '))
if km != 0 and km <= 200:
    custo = km * 0.50
    print(f'\nSua viagem vai custar R${custo:.2f}')
elif km == 0:
    print('Oh filho da puta, tu quer ir pra onde? ')
else:
    custo = km * 0.45
    print(f'Sua viagem vai custar R${custo:.2f}')
