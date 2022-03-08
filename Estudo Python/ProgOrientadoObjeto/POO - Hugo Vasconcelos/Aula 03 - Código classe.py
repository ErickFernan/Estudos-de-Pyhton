class MeuObjeto:
    def __init__(self, nome='Desconhecido', idade=-1):
        self.nome = nome
        self.idade = idade
        print('Chamando o construtor')

    def imprime(self):
        print(f'Olá meu nome é {self.nome} e eu tenho {self.idade} anos.')


p1 = MeuObjeto('Pedro', 6)
p1.imprime()
