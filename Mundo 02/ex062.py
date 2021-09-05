"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

barra = '\033[36m=\033[m' * 22
print(barra)
print('\033[35m10 TERMOS DE UMA P.A\033[m')
print(barra)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(termo, end='')
        print(' → ' if c <= total else ' = ', end='')
        termo += r
        c += 1
    print('PAUSA \033[31m◘\033[34m◘\033[30m◘')
    mais = int(input('Quantos termos a mais você quer ver? '))
print(f'FIM \033[31m☻\033[34m☻\033[30m☻\033[m, o total de termo foi {total}')
