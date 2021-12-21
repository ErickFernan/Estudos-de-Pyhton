class ValorRepetidoErro(Exception):
    def __str__(self):
        return 'Você já digitou esse valor'

def main():
    lista = []
    for i in range(0, 3):
        while True:
            try:
                num = int(input('Digite um número: '))

                if num not in lista:
                    lista.append(num)
                    print(lista)
                else:
                    raise ValorRepetidoErro  # Raise invoca um exceção

                break

            except ValueError:
                print('Digite apenas números.')



print(main())

