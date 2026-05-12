from src.domain.value_objects.produto_id import ProdutoId
from src.domain.value_objects.nome_produto import NomeProduto
from src.domain.value_objects.marca import Marca
from src.domain.value_objects.unidade import Unidade
from src.domain.value_objects.categoria_id import CategoriaId


class Produto:

    def __init__(
        self,
        produto_id: ProdutoId,
        nome: NomeProduto,
        marca: Marca,
        unidade: Unidade,
        categoria_id: CategoriaId
    ):

        self.__produto_id = produto_id
        self.__nome = nome
        self.__marca = marca
        self.__unidade = unidade
        self.__categoria_id = categoria_id

    @property
    def produto_id(self):
        return self.__produto_id

    @property
    def nome(self):
        return self.__nome

    @property
    def marca(self):
        return self.__marca

    @property
    def unidade(self):
        return self.__unidade

    @property
    def categoria_id(self):
        return self.__categoria_id

    def alterar_nome(
        self,
        novo_nome: NomeProduto
    ):

        self.__nome = novo_nome

    def alterar_marca(
        self,
        nova_marca: Marca
    ):

        self.__marca = nova_marca

    def alterar_unidade(
        self,
        nova_unidade: Unidade
    ):

        self.__unidade = nova_unidade

    def alterar_categoria(
        self,
        nova_categoria: CategoriaId
    ):

        self.__categoria_id = nova_categoria

    def to_dict(self):

        return {
            "id_produto": self.__produto_id.valor,
            "nome": self.__nome.valor,
            "marca": self.__marca.valor,
            "unidade": self.__unidade.valor,
            "categoria_id": self.__categoria_id.valor
        }

    @staticmethod
    def from_dict(data: dict):

        return Produto(
            produto_id=ProdutoId(data["id_produto"]),
            nome=NomeProduto(data["nome"]),
            marca=Marca(data["marca"]),
            unidade=Unidade(data["unidade"]),
            categoria_id=CategoriaId(
                data["categoria_id"]
            )
        )

    def __repr__(self):

        return (
            f"Produto("
            f"id={self.__produto_id.valor}, "
            f"nome='{self.__nome.valor}', "
            f"marca='{self.__marca.valor}', "
            f"unidade='{self.__unidade.valor}'"
            f")"
        )