"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

'''from time import sleep
notas = list()
dados = list()
while True:
    nome = dados.append(str(input('Nome: ')).strip())
    nota1 = dados.append(float(input('Nota 1: ')))
    nota2 = dados.append(float(input('Nota 2: ')))
    notas.append(dados[:])
    dados.clear()
    escolha = ' '
    while escolha not in 'NnSs':
        escolha = str(input('Continuar [S/N]: '))
    if escolha in 'Nn':
        break
print('-=' * 20)
print(f'{"No.":<5}', end='')
print(f'{"NOME":<25}', end='')
print(f'{"MÉDIA":<10}')
print('-' * 40)
for i, n in enumerate(notas):
    print(f'{i+1:<5}', end='')
    print(f'{n[0].title():<25}', end='')
    print(f'{(n[1] + n[2]) / 2:<10}')
print('-' * 40)
while True:
    op = int(input('Para mais detalhes:\nInforme o Nº do aluno, ou [999] para sair: '))
    if op == 999:
        print(f'{"FIM":=^40}')
        sleep(2)
        break
    else:
        op -= 1
        print(f'Notas de {notas[op][0].title()} são {notas[op][1]} e {notas[op][2]}')'''



ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

