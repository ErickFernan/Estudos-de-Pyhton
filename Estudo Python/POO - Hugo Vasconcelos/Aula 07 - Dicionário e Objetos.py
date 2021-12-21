Pessoa = {'Nome': 'Hugo', 'Profissão': 'Programador', 'Idade': 20}

Pessoa['Nome'] = 'Fábio'
print(Pessoa['Profissão'])
print(Pessoa['Nome'])

class Pessoa:
    pass

Hugo = Pessoa()
print(Hugo.__dict__)
