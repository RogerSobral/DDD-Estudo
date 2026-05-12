class ProdutoId:

    def __init__(self, valor: int):

        if valor <= 0:
            raise ValueError("ID inválido")

        self.valor = valor

    def __str__(self):
        return str(self.valor)