print('\033[35m-=\033[m'*30)
print('\033[36mAnalisador de Triângulos\033[m')
print('\033[35m-=\033[m'*30)
a = float(input('\033[31mPrimeiro segmento:\033[m'))
b = float(input('\033[32mSegundo segmento:\033[m'))
c = float(input('\033[33mTerceiro segmento:\033[m'))
if a-b < c < a+b and a-c < b < a+c and b-c < a < b+c:
    print('\033[30mOs segmentos acima podem formar um triângulo')
else:
    print('\033[30mOs segmentos acima não podem formar triângulo')
