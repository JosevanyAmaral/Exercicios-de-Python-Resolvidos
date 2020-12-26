print('-'*60)
print('{:^60}'.format('SEQUÊNCIA DE FIBONACCI'))
print('-'*60)
n = int(input('Quantos termos você quer mostrar? '))
print('~'*60)
f1 = 0
f2 = 1
f3 = 0
c = 3
if n == 0:
    print('Não serão mostrados termos')
elif n == 1:
    print('0', end=' → ')
elif n == 2:
    print('0 → 1 → ', end='')
else:
    print('0 → 1 → ', end='')
    while c <= n:
        f3 = f1 + f2
        print('{}'.format(f3), end=' → ')
        f1 = f2
        f2 = f3
        c += 1
print('FIM')
print('~'*60)
