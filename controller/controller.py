from model.model import ModeloCital
from view.view import VisualizacaoCital

class ControladorCital:
    def __init__(self, json_path: str):
        self.modelo = ModeloCital(json_path)
        self.visualizacao = VisualizacaoCital()

    def executar(self) -> None:
        self.visualizacao.exibir_pagina(
            total_por_item = self.modelo.obter_total_por_item(),
            receita_por_item = self.modelo.obter_receita_por_item(),
            vendas_por_data = self.modelo.obter_vendas_por_data(),
            receita_por_data = self.modelo.obter_receita_por_data(),
        )