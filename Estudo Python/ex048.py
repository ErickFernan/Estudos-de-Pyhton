c = 0
i = 0
for n in range(3, 500, 3):
    if n % 2 == 1:
        #print(n, end=' ')
        c += n
        i += 1
        #print(c, end=' ')
print('A soma será: \033[31m{}\033[m.'.format(c))
print('Foram somados: \033[31m{}\033[m números.'.format(i))
