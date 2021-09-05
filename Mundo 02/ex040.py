"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""

nota1 = float(input('Informe a 1ª nota do aluno: '))
nota2 = float(input('Informe a 2ª nota do aluno: '))
media = (nota1 + nota2) / 2
if 10 > media >= 7:
    print(f'Com media {media:.1f} o aluno está \033[4;34mAPROVADO!z033[m')
elif 5 <= media <= 6.9:
    print(f'Com media {media:.1f} o aluno está \033[1;32mEM RECUPERAÇÃO!\033[m')
elif 0 < media < 5:
    print(f'Com media {media:.1f} o aluno está \033[7;31mREPROVADO!!!\033[m')
else:
    print(f'Para se obter média {media:.2f} as notas informadas estão inválidas! Tente novamente!')