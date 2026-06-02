class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = 0
        self.set_preco(preco)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro: O preço não pode ser negativo.")

if __name__ == "__main__":
    prod = Produto("Notebook", 3500)
    print(f"Produto: {prod.get_nome()} | Preço: R${prod.get_preco()}")
    prod.set_preco(-10)
    prod.set_preco(3200)
    print(f"Novo preço: R${prod.get_preco()}")
