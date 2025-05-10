class Carro:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print("Carro ligado.")

    def desligar(self):
        self.ligado = False
        print("Carro desligado.")

c = Carro()

c.ligar()
c.desligar()