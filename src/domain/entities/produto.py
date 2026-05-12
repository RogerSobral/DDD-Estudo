from src.domain.value_objects.produto_id import ProdutoId
from src.domain.value_objects.dinheiro import Dinheiro
from src.domain.exceptions.produto_exception import ProdutoInvalidoException


class Produto:

    def __init__(
        self,
        produto_id: ProdutoId,
        nome: str,
        marca: str,
        valor: Dinheiro
    ):

        self._id = produto_id
        self._nome = nome
        self._marca = marca
        self._valor = valor

        self.validar()

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def marca(self):
        return self._marca

    @property
    def valor(self):
        return self._valor

    def alterar_nome(self, novo_nome):

        if not novo_nome:
            raise ProdutoInvalidoException("Nome inválido")

        self._nome = novo_nome

    def alterar_valor(self, novo_valor):

        self._valor = Dinheiro(novo_valor)

    def validar(self):

        if not self._nome:
            raise ProdutoInvalidoException("Nome obrigatório")

        if len(self._nome) < 2:
            raise ProdutoInvalidoException(
                "Nome deve possuir ao menos 2 caracteres"
            )

        if not self._marca:
            raise ProdutoInvalidoException("Marca obrigatória")

    def to_dict(self):

        return {
            "id": self._id.valor,
            "nome": self._nome,
            "marca": self._marca,
            "valor": self._valor.valor
        }