from src.application.dto.produto_dto import ProdutoDTO


class ListarProdutos:

    def __init__(self, repository):

        self.repository = repository

    def executar(self):

        produtos = self.repository.listar()

        return [
            ProdutoDTO(
                produto_id=produto.id.valor,
                nome=produto.nome,
                marca=produto.marca,
                valor=produto.valor.valor
            )
            for produto in produtos
        ]