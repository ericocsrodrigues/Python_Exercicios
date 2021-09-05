"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
"""
cont_mulheres = soma_idade = homem_velho = 0
nome_homem_velho = ''
for p in range(1, 5):
    print(f'------ {x}ª PESSOA ------')
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idade = int(input('Idade: '))
    soma_idade += idade
    if sexo == 'F':
        if idade < 20:
            cont_mulheres += 1
    if sexo == 'M':
        if idade > homem_velho:
            homem_velho = idade
            nome_homem_velho = nome

media = soma_idade / 4
print(media)
print(f'Temos {cont_mulheres} mulheres com idade inferior a 20 anos.')
print(f'O homem mais velho se chama {nome_homem_velho} e ele tem {homem_velho} anos')
"""

somaidade = 0
idadehomemvelho = 0
homemvelho = ''
contmulher = 0
for p in range(1, 5):
    print(f'------ {p}ª PESSOA ------')
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo [M/F]: ')).strip()
    idade = int(input('Idade: '))
    somaidade += idade
    if sexo in 'Mm' and idade > idadehomemvelho:
        idadehomemvelho = idade
        homemvelho = nome.title()
    if sexo in 'Ff' and idade < 20:
        contmulher +=1

media = somaidade / 4
print(f'A méida de idades é {media} anos')
print(f'O homem mais velho se chama {homemvelho} e tem {idadehomemvelho} anos.')
print(f'Temos {contmulher} com idade inferior a 20 anos')
