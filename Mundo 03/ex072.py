"""
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = 100
while n not in range(0, 21):
    n = int(input('Escolha um número de para vê-lo por extenso[0 a 20]: '))
print(lista[n])
