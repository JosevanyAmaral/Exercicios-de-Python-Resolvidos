a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número digitado foi {}'.format(menor))
# Verificando quem é o maior
maior = b
if a > b and a > c:
    maior = a
if c > a and c > b:
    maior = c
print('O maior número digitado foi {}'.format(maior))
