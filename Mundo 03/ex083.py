"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

'''frase = str(input('Digite uma expressão com parênteses: '))
lista = list(frase)
contabre = 0
contfecha = 0
for x in lista:
    if x == '(':
        contabre += 1
    elif x == ')':
        contfecha += 1
if contabre == contfecha:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')'''

exp = str(input('Digite uma expressão com parênteses: ')).strip()
lista = list()
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')


