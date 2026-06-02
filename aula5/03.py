class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus


gerente = Gerente("Fernanda", 6200, 1800)

gerente.exibir()
print(f"Bônus: R$ {gerente.bonus:.2f}")
print(f"Salário Total: R$ {gerente.salario_total():.2f}")
