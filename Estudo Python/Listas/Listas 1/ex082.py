lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    resp = input('Quer continar? [S/N] ').lower()
    lista.append(num)
    if resp != 's':
        break
print (lista)
val = 0
for n, val in enumerate(lista):
    if val % 2 == 0:
        pares.append(lista[n])
    else:
        impares.append(lista[n])
print(pares)
print(impares)