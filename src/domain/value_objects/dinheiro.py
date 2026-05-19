class Dinheiro:

    def __init__(self, valor: float):

        valor = float(valor)

        if valor <= 0:
            raise ValueError("Valor monetário inválido")

        self.__valor = round(valor, 2)

    @property
    def valor(self):
        return self.__valor 
    


    def __float__(self):
        return self.valor

    def __str__(self):
        return f"R$ {self.valor:.2f}"
    
    def build(self, valor: float):
        return Dinheiro(valor)