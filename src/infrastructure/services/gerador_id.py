import json
import os


class GeradorID:

    def __init__(
        self,
        caminho_arquivo="src/infrastructure/persistence/json/produtos.json"
    ):

        self.caminho_arquivo = caminho_arquivo

    def gerar(self):

        if not os.path.exists(self.caminho_arquivo):
            return 1

        with open(
            self.caminho_arquivo,
            "r",
            encoding="utf-8"
        ) as arquivo:

            try:
                dados = json.load(arquivo)
            except:
                return 1

        if not dados:
            return 1

        ultimo_id = max(item["id"] for item in dados)

        return ultimo_id + 1