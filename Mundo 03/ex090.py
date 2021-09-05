"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""
alunos = dict()
alunos['nome'] = str(input('Nome: ')).strip().title()
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if 10 >= alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado!'
elif 5 < alunos['media'] < 7:
    alunos['situacao'] = 'Em recuperação!'
elif alunos['media'] < 5:
    alunos['situacao'] = 'Reprovado!'

for v, i in alunos.items():
    print(f' - {v} é igual: {i}')
