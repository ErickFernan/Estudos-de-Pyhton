n = 0
while True:
    if n < 0:
        break
    n = int(input('Quer ver a tabuade de qual valor? '))
    print('_'*30)
    for i in range(1,11):
        print(f'{n} x {i} = {n * i}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO, Volte sempre!')

