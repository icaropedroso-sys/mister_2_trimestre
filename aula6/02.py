class Instrumento:
    def tocar(self):
        pass


class Violao(Instrumento):
    def tocar(self):
        print("Trim trim trim")


class Bateria(Instrumento):
    def tocar(self):
        print("Bum bum tss")


class Piano(Instrumento):
    def tocar(self):
        print("Lá si dó ré")


instrumentos = [Violao(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()
