class Unidade:

    UNIDADES_VALIDAS = [
        "UN",
        "KG",
        "G",
        "L",
        "ML",
        "CX",
        "PCT",
        "M"
    ]

    def __init__(self, valor: str):

        valor = valor.upper().strip()

        if valor not in self.UNIDADES_VALIDAS:
            raise ValueError(
                "Unidade inválida"
            )

        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def __eq__(self, other):

        if not isinstance(other, Unidade):
            return False

        return self.__valor == other.valor

    def __str__(self):
        return self.__valor