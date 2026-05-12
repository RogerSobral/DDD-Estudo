class Quantidade:


    def __init__(self, valor):

        valor = float(valor)

        if valor < 0:
            raise ValueError(
                "Quantidade não pode ser negativa"
            )

        self.__valor = round(valor, 2)


    @property
    def valor(self):
        return self.__valor


    def somar(self, valor):

        valor = float(valor)

        if valor <= 0:
            raise ValueError(
                "Valor deve ser maior que zero"
            )

        return Quantidade(
            self.__valor + valor
        )

    def subtrair(self, valor):

        valor = float(valor)

        if valor <= 0:
            raise ValueError(
                "Valor deve ser maior que zero"
            )

        novo_valor = self.__valor - valor

        if novo_valor < 0:
            raise ValueError(
                "Estoque insuficiente"
            )

        return Quantidade(novo_valor)

    def __float__(self):
        return self.__valor

    def __eq__(self, other):

        if not isinstance(other, Quantidade):
            return False

        return self.__valor == other.valor

    def __str__(self):
        return str(self.__valor)