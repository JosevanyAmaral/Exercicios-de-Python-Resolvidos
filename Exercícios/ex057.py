sexo = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo Inválido. Qual é o seu sexo? ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
