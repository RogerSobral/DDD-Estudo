class TipoMovimento:

    TIPOS_VALIDOS = [
        "ENTRADA",
        "SAIDA",
        "AJUSTE",
        "TRANSFERENCIA"
    ]

    def __init__(self, valor: str):

        valor = valor.upper().strip()

        if valor not in self.TIPOS_VALIDOS:
            raise ValueError(
                "Tipo de movimento inválido"
            )

        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def entrada(self):
        return self.__valor == "ENTRADA"

    def saida(self):
        return self.__valor == "SAIDA"

    def __eq__(self, other):

        if not isinstance(other, TipoMovimento):
            return False

        return self.__valor == other.valor

    def __str__(self):
        return self.__valor