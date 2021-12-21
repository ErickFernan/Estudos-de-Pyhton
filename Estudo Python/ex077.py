conjunto = ('aprender', 'programar', 'linguagem',
            'python','Curso')
for palavra in conjunto:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
