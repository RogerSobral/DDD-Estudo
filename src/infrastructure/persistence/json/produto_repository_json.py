import json
        with open(
            self.caminho_arquivo,
            "r",
            encoding="utf-8"
        ) as arquivo:

            try:
                return json.load(arquivo)
            except:
                return []

    def _salvar_arquivo(self, dados):

        with open(
            self.caminho_arquivo,
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    def salvar(self, produto):

        dados = self._ler_arquivo()

        dados.append(
            ProdutoMapper.to_dict(produto)
        )

        self._salvar_arquivo(dados)

    def listar(self):

        dados = self._ler_arquivo()

        return [
            ProdutoMapper.to_entity(item)
            for item in dados
        ]

    def buscar_por_id(self, produto_id):

        dados = self._ler_arquivo()

        for item in dados:

            if item["id"] == produto_id:
                return ProdutoMapper.to_entity(item)

        return None

    def atualizar(self, produto):

        dados = self._ler_arquivo()

        for index, item in enumerate(dados):

            if item["id"] == produto.id.valor:

                dados[index] = ProdutoMapper.to_dict(produto)

                break

        self._salvar_arquivo(dados)

    def deletar(self, produto_id):

        dados = self._ler_arquivo()

        novos_dados = [
            item
            for item in dados
            if item["id"] != produto_id
        ]

        self._salvar_arquivo(novos_dados)