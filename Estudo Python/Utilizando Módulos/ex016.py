#programa para ler um nº e mostrar a sua parte inteira
import math
#from math import trunc ----> outra opção

n = float(input('Digite um nº: '))
print('O número: {} tem a parte inteira {}.'.format(n, math.trunc(n)))
