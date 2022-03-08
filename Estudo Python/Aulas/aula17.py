num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
#num.pop(2) #sem nada remove o ultimo valor, com indice remove o indice
num.remove(2)#só retira o primeiro que ele achar
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2,3,4,7]
b = a[:] # se escrever a=b é feita uma ligação,então todas alterações acontecem nas duas listas
c = a
c[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')