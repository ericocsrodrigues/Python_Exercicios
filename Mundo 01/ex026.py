frase = str(input('\033[1;34mDigite um frase:\033[m ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes')
print(f'A primeira letra A aparecer na posição: {frase.find("A")+1}')
print(f'A última letra A apareceu na posição: {frase.rfind("A")+1}')