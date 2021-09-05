"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
precos = ('Lápis', 1.75,
          'Borracha', 2,
          'Caderno', 15.90,
          'Estojo', 25,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.3,
          'Livro', 34.9)
print(len(precos))
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for x in range(0, len(precos), 2):
    print(f'{precos[x]:.<30}', end='')
    print(f'{"R$"}', end=' ')
    print(f'{precos[x + 1]:>6.2f}')
print('-' * 40)
