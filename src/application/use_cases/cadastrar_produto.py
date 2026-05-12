from src.domain.entities.produto import Produto
from src.domain.value_objects.produto_id import ProdutoId
from src.domain.value_objects.dinheiro import Dinheiro
from src.domain.aggregates.produto_aggregate import ProdutoAggregate
from src.domain.services.produto_domain_service import ProdutoDomainService


class CadastrarProduto:

    def __init__(self, repository, gerador_id):

        self.repository = repository
        self.gerador_id = gerador_id

    def executar(self, nome, marca, valor):

        produtos = self.repository.listar()

        ProdutoDomainService.validar_nome_unico(
            produtos,
            nome
        )

        produto = Produto(
            produto_id=ProdutoId(
                self.gerador_id.gerar()
            ),
            nome=nome,
            marca=marca,
            valor=Dinheiro(valor)
        )

        aggregate = ProdutoAggregate(produto)

        self.repository.salvar(aggregate.produto)

        return aggregate.produto