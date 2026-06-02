class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = ""
        self.__idade = 0
        self.set_nome(nome)
        self.set_idade(idade)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome.strip():
            self.__nome = nome
        else:
            print("Erro: O nome não pode ser vazio.")

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else:
            print("Erro: Idade deve ser entre 0 e 120 anos.")

    def apresentar(self):
        print(f"Nome: {self.__nome} | Idade: {self.__idade} anos")

if __name__ == "__main__":
    p = Pessoa("Ana", 25)
    p.apresentar()
    p.set_idade(150)
    p.set_nome("")
    p.apresentar()
