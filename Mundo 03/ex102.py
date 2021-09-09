"""

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
    if show:
        f = 1
        for c in range(num, 1, -1):
            print(f'{c}', end=' x ')
            sleep(0.5)
            f *= c
        print(f'1 =', end=' ')
        return f
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


menu('Cálculo Fatorial')
fat = int(input('Digite um valor para ver seu fatorial: '))
print(fatorial(fat, True))
