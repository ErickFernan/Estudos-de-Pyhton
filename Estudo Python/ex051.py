pt = float(input('Primeiro termo: '))
q = float(input('Razão: '))
count = 0
for c in range(1, 11):
    aqui = pt + c*q
    print('{:.0f}'.format(aqui), end="→")
print('Acabou!')