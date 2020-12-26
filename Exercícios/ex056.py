totm = 0
maisvelho = 0
media = 0
nomemv = ''
for c in range(1, 5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:').strip())
    media += idade
    if c == 1 and sexo in 'Mm':
        maisvelho = idade
        nomemv += nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomemv = nome
    if sexo in 'Ff' and idade < 20:
        totm += 1
print('A média de idades do grupo é {:.1f}'.format(media/4))
print('O homem mais velho chama-se {} e tem {} anos'.format(nomemv, maisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm))
