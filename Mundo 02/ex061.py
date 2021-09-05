"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

barra = '\033[36m=\033[m' * 22
print(barra)
print('\033[35m10 TERMOS DE UMA P.A\033[m')
print(barra)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n
c = 1
while c <= 10:
    print(termo, end='')
    print(' → ' if c <= 10 else ' = ', end='')
    termo += r
    c += 1
print('FIM \033[31m☻\033[34m☻\033[30m☻')