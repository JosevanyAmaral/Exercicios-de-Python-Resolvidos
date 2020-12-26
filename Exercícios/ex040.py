nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média final é {:.1f} - \033[1;31mREPROVADO\033[m'.format(media))
elif 5 <= media <= 6.9:
    print('Sua media final é {:.1f} - \033[1;33mRECUPERAÇÃO\033[m'.format(media))
else:
    print('Sua média final é {:.1f} - \033[1;32mAPROVADO\033[m'.format(media))
