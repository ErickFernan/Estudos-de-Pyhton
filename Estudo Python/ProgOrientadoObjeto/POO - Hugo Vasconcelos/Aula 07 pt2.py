class Animal:
    def __init__(self, cor='', genero='', andar=0):
        self.cor = cor
        self.genero = genero
        self.num_de_patas = andar

    def falar(self):
        print('Olá sou um cachorro e sei falar.')

    def andar(self):
        print(f'Estou andando sobre {self.num_de_patas} patas.')

    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('Machos não amamentam.')
            return
        print('Amamentando meu filhote.')


# Rex = Animal('marron', 'macho', 4)
# Rex.falar()
# Rex.andar()
# Rex.amamentar()


class Pessoa(Animal):
    def __init__(self, cor='', genero='', andar=0, cabelo=''):
        super(Pessoa, self).__init__(cor, genero, andar)
        self.cabelo = cabelo

    def falar(self):
        super(Pessoa, self).falar()  # Super pega o valor de outro construtor, de outra classe externa.
        print('Olá sou um pessoa e sei falar.')


Hugo = Pessoa('branco', 'masculino', 2, 'castanho')
Hugo.falar()
