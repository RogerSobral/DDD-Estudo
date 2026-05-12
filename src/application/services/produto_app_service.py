class ProdutoAppService:

    def __init__(
        self,
        cadastrar_use_case,
        listar_use_case,
        buscar_use_case
    ):

        self.cadastrar_use_case = cadastrar_use_case
        self.listar_use_case = listar_use_case
        self.buscar_use_case = buscar_use_case

    def cadastrar(
        self,
        nome,
        marca,
        valor
    ):

        return self.cadastrar_use_case.executar(
            nome,
            marca,
            valor
        )

    def listar(self):

        return self.listar_use_case.executar()

    def buscar_por_id(self, produto_id):

        return self.buscar_use_case.executar(produto_id)