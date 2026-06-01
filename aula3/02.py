class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        novo_preco = self.preco - (self.preco * percentual / 100)
        return novo_preco


produto = Produto("bolacha", 67)

print("Nome:", produto.nome)
print("Preço original:", produto.preco)
print("Preço com desconto:", produto.desconto(10))
