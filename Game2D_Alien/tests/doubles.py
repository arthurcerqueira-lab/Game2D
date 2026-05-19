from src.desconto import IDesconto

class StubDesconto(IDesconto):
    def calcular(self, valor):
        return 0