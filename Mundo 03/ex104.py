"""
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""


def leiaint(frase):
    while True:
        x = input(frase)
        if x.isnumeric():
            return int(x)
        else:
            print(f'\033[31;40mERRO! Digite um número inteiro válido\033[m')


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
