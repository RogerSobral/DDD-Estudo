from src.domain.entities.produto import Produto
from src.domain.value_objects.dinheiro import Dinheiro


class ProdutoAggregate:

    def __init__(self, produto: Produto):

        self._produto = produto

    @property
    def produto(self):
        return self._produto

    def alterar_preco(self, novo_valor: Dinheiro):
        self._produto.alterar_valor(novo_valor=novo_valor)

        

    def alterar_nome(self, novo_nome):

        self._produto.alterar_nome(novo_nome)

    def dados(self):

        return self._produto.to_dict()
    