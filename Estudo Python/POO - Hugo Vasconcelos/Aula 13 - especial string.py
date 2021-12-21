class Conta:
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo

    def __str__(self):  # Devolve um string que pode ser formatada
        return f'ID: {self.ID}\nSaldo: R$ {self.saldo:.2f} '

    def __add__(self, other):  # Tem o método __sub__ __div__ __mult__ e mutb
        self.saldo += other.saldo


Bradesco = Conta(456, 2000)
print(Bradesco)

Itau = Conta(546, 3550)
print(Itau)
Itau + Bradesco
print(Itau.saldo)
