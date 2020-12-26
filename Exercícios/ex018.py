from math import sin, cos, tan, radians
angulo = int(input('Digite o valor do ângulo:'))
print('O Seno de {}° vale {:.3f}'.format(angulo, sin(radians(angulo))))
print('O Cosseno de {}° vale {:.3f}'.format(angulo, cos(radians(angulo))))
print('A Tangente de {}° vale {:.3f}'.format(angulo, tan(radians(angulo))))
