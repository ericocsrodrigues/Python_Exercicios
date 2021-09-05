"""
Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

medida = float(input('Informe um distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida de \033[1;34m{medida}\033[mm corresponde a \033[7;30m{cm:.0f}\033[mcm e \033[7;30m{mm:.0f}\033[mmm')
