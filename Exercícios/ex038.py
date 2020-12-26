n1 = int(input('Digite o primero número:'))
n2 = int(input('Digite o segundo número:'))
if n1 > n2:
    print('O primeiro valor é \033[35mmaior\033[m.')
elif n2 > n1:
    print('O segundo valor é \033[36mmaior\033[m.')
else:
    print('Não existe valor maior, os dois são \033[32miguais\033[m.')
