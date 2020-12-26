peso = float(input('Quantos quilos você pesa? '))
altura = float(input('Quantos metros você tem? '))
IMC = peso/altura ** 2
if IMC < 18.5:
    print('\033[1;36mIMC = {:.1f} - ABAIXO DO PESO'.format(IMC))
elif 18.5 <= IMC < 25:
    print('\033[1;35mIMC = {:.1f} - PESO IDEAL'.format(IMC))
elif 25 <= IMC < 30:
    print('\033[1;34mIMC = {:.1f} - SOBREPESO'.format(IMC))
elif 30 <= IMC <= 40:
    print('\033[1;33mIMC = {:.1f} - OBESIDADE'.format(IMC))
else:
    print('\033[1;32mIMC = {:.1f} - OBESIDADE MÓRBIDA'.format(IMC))
print('Cuide da sua sua saúde, é o seu bem mais precioso.')
