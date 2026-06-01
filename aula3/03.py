class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 67

    def frear(self):
        self.velocidade -= 67

        if self.velocidade < 0:
            self.velocidade = 0


carro = Carro("SW4", "tiggo8pro_turbo")

carro.acelerar()
carro.acelerar()
carro.acelerar()

carro.frear()

print("Velocidade final:", carro.velocidade)
