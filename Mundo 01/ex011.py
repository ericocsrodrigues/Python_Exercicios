"""
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = a * l
print(f'Sua parede tem dimensão de \033[0;34m{l}\033[mx\033[0;34m{a}\033[m e sua área é de \033[4;35m{area}\033[mm².')
print(f'Para pintar essa parede, você vai precisar de \033[7;30m{area / 2}\033[mL de tinra')
