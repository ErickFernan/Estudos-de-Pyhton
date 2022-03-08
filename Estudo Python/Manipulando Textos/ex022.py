nome = input('Digite seu nome completo: ')

apenasletras = nome.replace(" ","")
dividido = nome.split()
primeironome = dividido[0]

print('''Em maiusculo: {}
Em minúsculo: {}
Nº de letras total: {}
Nº de letras primeiro nome: {}
'''.format(nome.upper(),nome.lower(),len(apenasletras),len(primeironome)))