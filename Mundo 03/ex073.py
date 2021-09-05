"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

seria_a = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamento', 'Athletico-PR', 'Atlético-GO', 'Ceará', 'Internacional', 'Santis', 'Corinthians', 'Juventudo', 'Bahia', 'São Paulo', 'Fluminense', 'Cuiabá', 'Sport', 'América-MG', 'Grêmio', 'Chapecoense')
print(f'Os 5 primeiros colocados são: ', seria_a[0:5])
print(f'Os 4 últimos colocados são: ', seria_a[-4:])
print(f'{sorted(seria_a)}')
print(f'O Chepcoense está na {seria_a.index("Chapecoense") + 1}º posição')

