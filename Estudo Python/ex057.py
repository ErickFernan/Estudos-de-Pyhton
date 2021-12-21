sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo [M/F]: ').upper().strip()[0]
    print(sexo)