"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

vel = int(input('Informe a velocidade do carro: '))
if vel > 80:
    d = vel - 80
    multa = 7 * d
    print(f'Você foi multador pois passou a {vel}km/h.\nValor da multa: R${multa:.2f}')
else:
    print('Você dirige que nem um velha!!! ')
