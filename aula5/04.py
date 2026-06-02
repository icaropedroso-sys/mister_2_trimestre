class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(
            f"Aluno: {self.nome} | Idade: {self.idade} | Matrícula: {self.matricula}"
        )


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(
            f"Professor: {self.nome} | Idade: {self.idade} | Salário: R$ {self.salario:.2f}"
        )


pessoas = [
    Aluno("Lucas", 19, "A1050"),
    Professor("Ricardo", 50, 6800),
    Aluno("Beatriz", 21, "A1051"),
    Professor("Patrícia", 42, 7200),
]

for pessoa in pessoas:
    pessoa.apresentar()
