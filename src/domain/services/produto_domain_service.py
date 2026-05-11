"""
DOMAIN SERVICE

Domain Service é usado quando:

a regra não pertence totalmente à entidade
envolve mais de uma entidade
lógica de domínio complexa

"""

class ProdutoDomainService:

    @staticmethod
    def validar_nome_unico(produtos, nome):
        for produto in produtos:
            if produto.nome == nome:
                raise ValueError("Produto já existe")