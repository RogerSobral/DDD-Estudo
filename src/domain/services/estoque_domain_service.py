class   EstoqueDomainService:
    

    @staticmethod
    def verificar_estoque_suficiente(estoque, quantidade):
        if estoque.quantidade.valor < quantidade.valor:
            raise ValueError("Quantidade insuficiente em estoque para saída")
        
    @staticmethod
    def verificar_produto_existe(estoque, produto_id):
        if estoque.produto_id.valor != produto_id.valor:
            raise ValueError("Produto não encontrado no estoque")