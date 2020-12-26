print('\033[35m-=\033[m' * 30)
print('\033[36mAnalisador de Triângulos\033[m')
print('\033[35m-=\033[m' * 30)
a = float(input('\033[31mPrimeiro segmento:\033[m'))
b = float(input('\033[32mSegundo segmento:\033[m'))
c = float(input('\033[33mTerceiro segmento:\033[m'))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('\033[30mOs segmentos acima podem formar um triângulo equilátero\033[m')
    elif a == b != c or a == c != b or b == c != a:
        print('\033[30mOs segmentos acima podem formar um triângulo isósceles\033[m')
    else:
        print('\033[30mOs segmentos acima podem formar um triângulo escaleno\033[m')
else:
    print('\033[30mOs segmentos acima não podem formar triângulo\033[m')
# \n - quebra linhas end = '' concatena com a linha à seguir
