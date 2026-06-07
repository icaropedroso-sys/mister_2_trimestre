class Funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        self.__nome = nome
        self.__matricula = matricula
        self.__salario_fixo = salario_fixo

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_salario_fixo(self):
        return self.__salario_fixo

    def set_salario_fixo(self, salario):
        if salario >= 0:
            self.__salario_fixo = salario
        else:
            print("Erro: salário não pode ser negativo!")

    def calcular_salario(self):
        pass

    def exibir(self):
        print(f"Nome: {self.get_nome()} | Matrícula: {self.get_matricula()} | "
              f"Tipo: {self.__class__.__name__} | "
              f"Salário: R$ {self.calcular_salario():.2f}")

class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo()

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, vendas):
        super().__init__(nome, matricula, salario_fixo)
        self.__vendas = vendas

    def calcular_salario(self):
        return self.get_salario_fixo() + (self.__vendas * 0.10)

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo() + 1500

funcionarios = [
    CLT("Ana", "001", 3000),
    Vendedor("Bruno", "002", 2000, 12000),
    Gerente("Carla", "003", 5000)
]

for funcionario in funcionarios:
    funcionario.exibir()
