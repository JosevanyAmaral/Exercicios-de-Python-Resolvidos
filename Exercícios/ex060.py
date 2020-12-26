numero = int(input('Digite um número para calcular o fatorial: '))
c = 0
fatorial = 1
print('{}! = '.format(numero), end='')
while c <= numero - 1:
    print('{}'.format(numero-c), end='')
    print(' x 'if c < numero - 1 else ' = ', end='')
    c += 1
    fatorial *= c
print('{}'.format(fatorial))
