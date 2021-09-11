"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.
"""
from BibliotecaCm7.menu import menu, lin
from time import sleep


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: número a ser calcula
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            sleep(0.5)
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
            f *= c

    return f


menu('Cálculo Fatorial')
fat = int(input('Digite um valor para ver seu fatorial: '))
lin()
print(fatorial(fat, True))
