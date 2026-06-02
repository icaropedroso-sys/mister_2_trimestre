class Pagamento:
    def processar(self, valor):
        return valor


class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 0.95


class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 1.02


class Pix(Pagamento):
    def processar(self, valor):
        return valor


pagamentos = [
    Dinheiro(),
    Cartao(),
    Pix()
]

valor = 250

for pagamento in pagamentos:
    print(f"Valor final: R$ {pagamento.processar(valor):.2f}")
