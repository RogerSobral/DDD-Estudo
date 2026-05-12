class ProdutoDTO:

    def __init__(
        self,
        produto_id,
        nome,
        marca,
        valor
    ):

        self.id = produto_id
        self.nome = nome
        self.marca = marca
        self.valor = valor

    def to_dict(self):

        return {
            "id": self.id,
            "nome": self.nome,
            "marca": self.marca,
            "valor": self.valor
        }