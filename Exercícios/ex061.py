primeiro = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite o valor da razão: '))
termo = primeiro
c = 1
print('Os 10 primeiros termos da P.A são: ')
while c <= 10:
    print(termo, end=' → ')
    termo += razao
    c += 1
print('FIM')
