"""
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians
ang = float(input('Informe o valor do ângulo: '))
se = sin(radians(ang))
co = cos(radians(ang))
tg = tan(radians(ang))
print(f'Para o ângulo de {ang}º o valor do seno é {se:.2f}, do cosseno é {co:.2f}, e da tangente é {tg:.2f}')
