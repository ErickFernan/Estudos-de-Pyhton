lista = list()
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]: #primeira iteração ou maior q o ultimo valor
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if lista[pos] >= num:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-'*30)
print(f'Os valores digitados em ordem foram: {lista}')
