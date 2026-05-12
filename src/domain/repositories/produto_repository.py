"""O domínio NÃO conhece JSON.

Então criamos apenas um contrato:
"""
from abc import ABC, abstractmethod


class ProdutoRepository(ABC):

    @abstractmethod
    def salvar(self, produto):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def buscar_por_id(self, produto_id):
        pass

    @abstractmethod
    def atualizar(self, produto):
        pass

    @abstractmethod
    def deletar(self, produto_id):
        pass