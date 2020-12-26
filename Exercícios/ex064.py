n = soma = numeros_Digitados = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        numeros_Digitados += 1
print('Você digitou {} e a soma deles foi: {}'.format(numeros_Digitados, soma))
