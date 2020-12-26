def LeiaDinheiro(msg):
    while True:
        preco = str(input(msg)).strip().replace(',', '.')
        if preco.isalpha() or preco == '':
            print(f'\033[1;31mERRO! "{preco}" é um preço inválido!\033[m')
        else:
            break
    return float(preco)
