"""
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
barra = '\033[36m=\033[m' * 22
print(barra)
print('\033[35m10 TERMOS DE UMA P.A\033[m')
print(barra)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = n + (10 - 1) * r
for x in range(n, decimo + r, r):
    print(x, end='-> ')
print('ACABABOU!')
