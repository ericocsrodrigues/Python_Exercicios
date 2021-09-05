"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
# Sem o for e com o replace

frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(" ", "")
invertido = frase[::-1]
print(f'O inverso de {junto} é {invertido}')
if invertido == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não forma um palíndromo')

# Com o for e com o split/join

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''
for letra in range(len(junto) - 1, -1, -1):
    invertido += junto[letra]
print(f'O inverso de {junto} é {invertido}')
if invertido == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não forma um palíndromo')

"""
frase = str(input('Digite uma frase: ')).strip().upper()  # Recebendo a frase
palavras = frase.split()  # Separando toda a frase por palavras
junto = ''.join(palavras)  # Unindo as frases sem espaços
# frase = frase.replace(" ", "")
# finvertido = frase[::-1]
invertido = ''
for letra in range(len(junto) - 1, -1, -1):  # Vou fazer um coisa x vezes, onde o x é o tamanho da frase sem espaço, só que de trás pra frente
#   print(junto[letra], end='#')  # Vou escrever a palavra junto na posição do for
    invertido += junto[letra]
print(f'O inverso de {junto} é {invertido}')
if invertido == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não forma um palíndromo')
"""