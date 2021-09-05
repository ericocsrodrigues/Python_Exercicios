"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'python', 'gratis', 'dev', 'curso', 'estudar', 'praticar', 'exercicio', 'trabalhar', 'programador', 'futuro')
for n in palavras:
    print(f'\nNa palavra {n.upper()} temos: ', end= ' ')
    for x in n:
        if x in 'AaEeIiOoUu':
            print(f'{x}', end = ' ')
