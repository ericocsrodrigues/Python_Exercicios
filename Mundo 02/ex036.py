"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Em quantos anos pretende pagar pela casa? '))
prazo = anos * 12
limite = salario * 0.3
prestacao = casa / prazo
if prestacao > limite:
    print(f'O empréstimo \033[7;30mNÂO\033[m aprovado! ')
else:
    print(f'O empréstimo foi \033[7;30mAPROVADO!\033[m ')
print(prestacao, limite)
