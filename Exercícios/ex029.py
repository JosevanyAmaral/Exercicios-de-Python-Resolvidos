vel = int(input('Qual é a velocidade do carro? (Km/h) '))
if vel > 80:
    print('O senhor foi multado por excesso de velocidade, a multa vai custar R${:.2f}'.format((vel-80)*7))
print('Tenha um bom dia.')
