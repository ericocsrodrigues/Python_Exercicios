"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
computador = randint(0, 100)
print('\033[31mSou seu computador...E este é um jogo de adivinhação. Eu escolhi um número entre 0 e 100.')
print('Será que consegue adivinhar?\033[m')
cont = 0
acertou = False
while not acertou:
    jogador = int(input('\033[34mQual é o seu palpite: '))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('\033[35mMenos...Tente mais um vez: ')
        elif jogador < computador:
            print('\033[31mMais...Tente mais uma vez: ')
print(f'\033[36mVocê acertou e precisou de {cont} tentativas.')
