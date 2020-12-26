times_brasileirao2020 = ('Atlético Mineiro', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco da Gama', 'Flamengo',
                         'Santos', 'Chapecoense', 'Fortaleza', 'Atlético Paranaense', 'Fluminense', 'Ceará',
                         'Atlético Goianiense', 'Grêmio', 'Corinthians', 'Coritiba', 'Bragantino', 'Botafogo', 'Goiás',
                         'Bahia')
print(f'Lista de times do Brasileirão: {times_brasileirao2020}')
print(f'Os 5 primeiros classificados são: {times_brasileirao2020[:5]}')
print(f'Os 4 últimos classificados são: {times_brasileirao2020[16:]}')
print(f'Times em ordem alfabética: {sorted(times_brasileirao2020)}')
print(f'A Chapecoense está na {times_brasileirao2020.index("Chapecoense")+1}º posição')
