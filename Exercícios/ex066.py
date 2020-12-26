soma = tot_numdigitados = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    tot_numdigitados += 1
print(f'Foram digitados {tot_numdigitados} números e a soma entre eles vale {soma}!')
