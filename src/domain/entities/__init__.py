class Produto:

    def __init__(self, produto_id, nome, marca, valor):
        self._id = produto_id
        self._nome = nome
        self._marca = marca
        self._valor = valor

        self.validar()

    def validar(self):
        if not self._nome:
            raise ValueError("Nome obrigatório")

        if float(self._valor) <= 0:
            raise ValueError("Valor inválido")