"""
Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

c = float(input('Informe um temperatura em ºC: '))
f = ((9 * c) / 5) + 32
print(f'A temperatura de \033[1;31m{c}ºC\033[m corresponde a \033[4;34m{f}ºF\033[m.')