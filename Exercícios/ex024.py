cidade = str(input('Em que cidade você nasceu? ')).strip().title()
dividido = cidade.split()
print('Santo' in dividido[0])
#print(cidade[:6].capitalize() == 'Santo')
