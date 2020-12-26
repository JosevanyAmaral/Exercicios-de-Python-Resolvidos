qtd = int(input('Por quantos dias o carro foi alugado?\nR:'))
km = float(input('Quantos Quilómetros o carro percorreu?\nR:Km '))
print('O total a pagar é de R${:.2f}'.format((qtd * 60) + (0.15 * km)))
