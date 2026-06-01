class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto1 = Produto("esteira", 6767)
produto2 = Produto("peixe", 24)

print("Produto 1:")
print("Nome:", produto1.nome)
print("Preço:", produto1.preco)

print()

print("Produto 2:")
print("Nome:", produto2.nome)
print("Preço:", produto2.preco)
