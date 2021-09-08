"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
"""
from BibliotecaCm7.menu import menu


def area(l, c):
    a = l * c
    print(f'A área do terreno de {l}m x {c}m é {l * c}m²')


menu('Contorle de terrenos')
l = float(input('Informe a largura do terreno [m]: '))
c = float(input('Informe o comprimento do terreno [m]: '))
area(l, c)


