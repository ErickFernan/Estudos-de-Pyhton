def escreva(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(f'{texto:^{tam}}')
    print('~' * tam)


# início:
msg = ('Gustavo Guanabara', ' Curso de Python', 'CeV')
for v in msg:
    escreva(v)
