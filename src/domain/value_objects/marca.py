class Marca:

    def __init__(self, valor: str):

        valor = valor.strip()

        if len(valor) < 2:
            raise ValueError(
                "Marca inválida"
            )

        if len(valor) > 50:
            raise ValueError(
                "Marca muito grande"
            )

        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def __eq__(self, other):

        if not isinstance(other, Marca):
            return False

        return (
            self.__valor.lower()
            == other.valor.lower()
        )

    def __str__(self):
        return self.__valor