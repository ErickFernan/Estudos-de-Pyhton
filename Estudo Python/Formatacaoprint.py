
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
#Aparece a exclamação com 20 espaços de distância
print('Prazer em te conhecer {:>20}!'.format(nome))
#alinha a direita
print('Prazer em te conhecer {:<20}!'.format(nome))
#alinha a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome))
#centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome))
#preenche com =

print(nome*5)

n1 = int(input('num 1 = '))
n2 = int(input('num 2 = '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e \npotência {}.'.format(di, e))
