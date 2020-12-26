maior_18 = tot_Homens = mulheres_menores20 = 0
while True:
    print('{:-^60}'.format('Cadastre uma pessoa'))
    idade = int(input('Idade: '))
    if idade > 18:
        maior_18 += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo[0] not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'M':
        tot_Homens += 1
    if sexo in 'F' and idade < 20:
        mulheres_menores20 += 1
    resposta = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Ao todo temos {tot_Homens} homem cadastrado'if tot_Homens == 1
      else f'Ao todo temos {tot_Homens} homens cadastrados')
print(f'Temos {mulheres_menores20} mulher com menos de 20 anos'if mulheres_menores20 == 1
      else f'Temos {mulheres_menores20} mulheres com menos de 20 anos')
