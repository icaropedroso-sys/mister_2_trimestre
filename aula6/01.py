class Funcionario:
    def calcular_salario(self):
        return 0


class Vendedor(Funcionario):
    def __init__(self, salario_fixo, comissao):
        self.salario_fixo = salario_fixo
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario_fixo + self.comissao


class Gerente(Funcionario):
    def __init__(self, salario_fixo, bonus):
        self.salario_fixo = salario_fixo
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_fixo + self.bonus


vendedor = Vendedor(3200, 700)
gerente = Gerente(6800, 2200)

print(f"Salário do vendedor: R$ {vendedor.calcular_salario():.2f}")
print(f"Salário do gerente: R$ {gerente.calcular_salario():.2f}")
