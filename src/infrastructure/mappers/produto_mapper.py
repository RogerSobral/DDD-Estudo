from src.domain.entities.produto import Produto
from src.domain.value_objects.produto_id import ProdutoId
from src.domain.value_objects.dinheiro import Dinheiro


class ProdutoMapper:

    @staticmethod
    def to_entity(data):

        return Produto(
            produto_id=ProdutoId(data["id"]),
            nome=data["nome"],
            marca=data["marca"],
            valor=Dinheiro(data["valor"])
        )

    @staticmethod
    def to_dict(produto):

        return {
            "id": produto.id.valor,
            "nome": produto.nome,
            "marca": produto.marca,
            "valor": produto.valor.valor
        }