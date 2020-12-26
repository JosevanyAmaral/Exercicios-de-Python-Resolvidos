print('=' * 40)
print(f'\033[1;36m{"ATM EXPRESS":^40}\033[m')
print('=' * 40)
valor = int(input('Quanto pretende levantar? AOA'))
total = valor
totnotas = 0
notas = 5000
while True:
    if valor > 50000:
        print('O seu banco não lhe permite levantar mais de AOA50000 por dia')
        break
    if total >= notas:
        total -= notas
        totnotas += 1
    else:
        if totnotas > 0:
            print(f'Total de {totnotas} nota de AOA{notas:.2f}'if totnotas == 1
                  else f'Total de {totnotas} notas de AOA{notas:.2f}')
        if notas == 5000:
            notas = 2000
        elif notas == 2000:
            notas = 1000
        totnotas = 0
        if total == 0:
            print('='*40)
            break
print('Volte sempre ao ATM EXPRESS. Tenha um bom dia!')
