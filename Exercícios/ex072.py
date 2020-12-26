extensao = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if not 0 <= n <= 20:
        n = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extensao[n]}')
    resp = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    while resp[0] not in 'SN':
        resp = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if resp[0] in 'N':
        break
