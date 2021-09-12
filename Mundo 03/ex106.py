"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e
o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""
from time import sleep
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[1;30;107m'     # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 1)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo("SISTEMA DE AJUDA PYTHONICA", 6)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        titulo('>>>Até Logo!<<<', 4)
        break
    else:
        ajuda(comando)
