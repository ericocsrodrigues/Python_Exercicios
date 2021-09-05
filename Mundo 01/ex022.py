nome = str(input('Informe seu nome completo: ')).strip()
print(f'Seu nome em maiúsculo fica: {nome.upper()}')
print(f'\nSeu nome em minúsculo fica: {nome.lower()}')

# nome1 = nome.replace(" ","")
print(f'\nSeu nome sem espaços fica: {nome} e ele tem {len(nome) - nome.count(" ")} caracteres')

# nome2 = nome.split()
# print(f'\nSeu primeiro nome é: {nome2[0]} e ele tem: {len(nome2[0])} caracteres')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
