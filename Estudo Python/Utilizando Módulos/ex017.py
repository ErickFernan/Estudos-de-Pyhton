#Programa recebe os catetos e retorna hipotenusa

import math

co = float(input('Entre com o cateto oposto: '))
ca = float(input('Entre com o cateto adjacente: '))
hip = math.hypot(co, ca)
print('O valor da hipotenusa é: {:.0f}.'.format(hip))
