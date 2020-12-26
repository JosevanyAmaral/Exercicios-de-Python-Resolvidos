distancia = int(input('Qual será a distância da sua viagem? Km/h  '))
if distancia <= 200:
    print('O custo da sua viagem são R${:.2f}'.format(distancia * 0.50))
else:
    print('O custo da sua viagem são R${:.2f}'.format(distancia * 0.45))
