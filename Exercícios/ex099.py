def maior(* lista):
    from time import sleep
    print('-='*20)
    print('Analisando os valores passados...')
    for c in range(0, len(lista)):
        print(lista[c], end=' ')
        sleep(0.3)
    print(f'Foram informados {len(lista)} valores ao todo.')
    if len(lista) == 0:
        lista = [0]
    print(f'O maior valor informado foi {max(lista)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
