from src.domain.exceptions.produto_exception import (
    ProdutoNaoEncontradoException
)


class BuscarProduto:

    def __init__(self, repository):

        self.repository = repository

    def executar(self, produto_id):

        produto = self.repository.buscar_por_id(produto_id)

        if not produto:
            raise ProdutoNaoEncontradoException(
                "Produto não encontrado"
            )

        return produto