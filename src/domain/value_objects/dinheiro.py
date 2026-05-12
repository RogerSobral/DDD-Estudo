class Dinheiro:

    def __init__(self, valor: float):

        valor = float(valor)

        if valor <= 0:
            raise ValueError("Valor monetário inválido")

        self.valor = round(valor, 2)

    def __float__(self):
        return self.valor

    def __str__(self):
        return f"R$ {self.valor:.2f}"