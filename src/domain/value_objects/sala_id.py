class SalaId:

    def __init__(self, valor: int):

        if valor <= 0:
            raise ValueError(
                "Sala inválida"
            )

        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def __eq__(self, other):

        if not isinstance(other, SalaId):
            return False

        return self.__valor == other.valor

    def __str__(self):
        return str(self.__valor)