

from src.domain.value_objects.quantidade import Quantidade
from src.domain.value_objects.tipo_movimento import TipoMovimento


class Movimentacao:
    def __init__(self, produto_id, quantidade:Quantidade, tipo:TipoMovimento):
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.tipo = tipo  # 'entrada' ou 'saida'


    
    
    def validar_movimentacao(self, estoque):
        if self.tipo == TipoMovimento.SAIDA and estoque.quantidade.valor < self.quantidade.valor:
            raise ValueError("Quantidade insuficiente em estoque para saída")

# explicar usando strategy pattern 

    def aplicar_movimentacao(self, estoque):
        if self.tipo == TipoMovimento.ENTRADA:
            estoque.entrada_estoque(self.quantidade)
        elif self.tipo == TipoMovimento.SAIDA:
            estoque.saida_estoque(self.quantidade)
        else:
            raise ValueError("Tipo de movimentação inválido")   



    def to_dict(self):
        return {
            "produto_id": self.produto_id,
            "quantidade": self.quantidade.valor,
            "tipo": self.tipo.valor
        }
    
    @staticmethod
    def from_dict(data):
        return Movimentacao(
            produto_id=data["produto_id"],
            quantidade=Quantidade(data["quantidade"]),
            tipo=TipoMovimento(data["tipo"])
        )