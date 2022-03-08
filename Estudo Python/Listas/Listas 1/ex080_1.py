lista = []
n = 0
val = 0
for n in range(0,5):
    val = int(input('Valor: '))
    if n == 0 or val > lista[-1]:
        lista.append(val)
    else:
        pos = 0
        while pos < len(lista):
            if val <= lista[pos]:
                lista.insert(pos, val)
                break
            pos += 1
print(lista)