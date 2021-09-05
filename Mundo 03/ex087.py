"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
pares = contpar = somacoluna = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))
print('\033[31m-=\033[m' * 11)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
    print()
print('\033[34m-=\033[m' * 11)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            contpar += 1
            pares += matriz[l][c]
for l in range(0, 3):
    somacoluna += matriz[l][2]

print(f'Foram digitados {contpar} valores pares e a soma vale {pares}')
print(f'a soma dos elemnetos da 3ª coluna é: {somacoluna}')
print(f'O maior valor da linha 2 é: {max(matriz[1])}')

