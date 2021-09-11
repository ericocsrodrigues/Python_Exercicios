"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""


def notas(*args, sit=False):
    """
    -> Função que vai receber notas e retornar, atravez de um dicionário, a situação das notas de um turma
    :param args: entrada de notas
    :param sit: argumento True/False pora ativar a situação da turma
    :return: dicionário com quantidade de notas, maior nota, menor nota, média da turma
    """
    turma = dict()
    turma['qtd_notas'] = len(args)
    turma['maior_nota'] = max(args)
    turma['menor_nota'] = min(args)
    turma['media_turma'] = sum(args) / len(args)
    if sit:
        if turma['media_turma'] >= 7:
            turma['situação'] = 'EXCELENTE'
        elif 5 < turma['media_turma'] < 7:
            turma['situação'] = 'PREOCUPANTE'
        else:
            turma['situação'] = 'CRÍTICA'
    print(turma)


notas(7.6, 5.6, 10, 9.8, 8, 6.5, 10, 1.3, 10, 10, 9.4, sit=True)

