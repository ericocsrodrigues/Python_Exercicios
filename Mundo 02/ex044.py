"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""

valor = float(input('Informe o valor do item: R$'))
print('Escolha a forma de pagamento: ')
print('''[ 1 ] - À vista dinheiro ou cheque.
[ 2 ] - À vista cartão.
[ 3 ] - 2x no cartão.
[ 4 ] - 3x ou mais no cartão.''')
forma = int(input('\033[4;34mOpção:\033[m '))
if forma == 1:
    print(f'O produto que custa \033[0;32m{valor:.2f}\033[m nessa forma de pagamento custará \033[4;34m{(valor * 0.9):.2f}\033[m')
elif forma == 2:
    print(f'O produto que custa \033[0;32m{valor:.2f}\033[m nessa forma de pagamento custará \033[4;34m{(valor * 0.95):.2f}\033[m')
elif forma == 3:
    print(f'O produto que custa \033[0;32m{valor:.2f}\033[m nessa forma de pagamento não sofre alteração de preço')
elif forma == 4:
    print(f'O produto que custa \033[0;32m{valor:.2f}\033[m nessa forma de pagamento custará \033[4;31m{(valor * 1.2):.2f}\033[m')
else:
    print('Opção invalida. Tente novamente!')
