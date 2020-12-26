cont = media = menor = maior = 0
resposta = ''
while resposta != 'N':
    n = int(input('Digite um número: '))
    cont += 1
    media += n
    if cont == 1:
        menor = maior = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if 'S' != resposta != 'N':
        print('Comando Inválido!')
        quit(1)
print('A média entre todos os valores foi: {:.1f}'.format(media/cont))
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
