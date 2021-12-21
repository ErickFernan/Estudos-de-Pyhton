num = int(input('Digite um nº entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000

print('''Seu nº é : {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
'''.format(num,u,d,c,m))

