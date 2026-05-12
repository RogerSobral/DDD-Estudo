from src.domain.entities.produto import Produto


class ProdutoAggregate:

    def __init__(self, produto: Produto):

        self._produto = produto

    @property
    def produto(self):
        return self._produto

    def alterar_preco(self, novo_valor):

        self._produto.alterar_valor(novo_valor)

    def alterar_nome(self, novo_nome):

        self._produto.alterar_nome(novo_nome)

    def dados(self):

        return self._produto.to_dict()
    