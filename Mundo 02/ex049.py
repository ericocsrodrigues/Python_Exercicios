"""
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

x = int(input('\033[32mInforme um número para saber a tabuada:\033[m '))
for y in range(1, 11):
    print(f'{x} x {y:2} = \033[4;34m{x * y}\033[m')
