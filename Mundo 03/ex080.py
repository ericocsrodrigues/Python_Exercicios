"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = list()
for c in range(5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > lista[-1]:
        lista.append(v)
        print(f'Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print('=' * 50)
print(f'Os valores digitados em ordem foram: {lista}')



