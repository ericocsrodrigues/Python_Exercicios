"""
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
dias = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantas km foi percorrido com o carro?'))
pdias = dias * 60
pkm = km * 0.15
total = pdias + pkm
print(f'O carro ficou locado por \033[1;31m{dias} dias\033[m e percorreu \033[1;31m{km:.1f}km\033[m. Totalizando \033[4;34mR${total:.2f}\033[m')
