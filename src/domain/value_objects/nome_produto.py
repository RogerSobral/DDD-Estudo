class NomeProduto:

    def __init__(self, valor: str):

        valor = valor.strip()

        if len(valor) < 3:
            raise ValueError(
                "O nome do produto deve ter "
                "no mínimo 3 caracteres"
            )

        if len(valor) > 100:
            raise ValueError(
                "O nome do produto é muito grande"
            )

        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def __eq__(self, other):

        if not isinstance(other, NomeProduto):
            return False

        return (
            self.__valor.lower()
            == other.valor.lower()
        )

    def __str__(self):
        return self.__valor