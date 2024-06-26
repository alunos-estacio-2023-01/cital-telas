import pandas as pd
import json

class ModeloCital:
    def __init__(self, json_path: str):
        with open(json_path) as f:
            data = json.load(f)

        try:
            self.df = pd.json_normalize(data, record_path=['itens'], meta=['numero_n_fe', 'data', 'forma_pagamento'])
        except pd.errors.ParserError:
            raise ValueError(f"Erro ao processar o arquivo json")

        self.df['data'] = pd.to_datetime(self.df['data'], utc=True)
        self.df['receita'] = self.df['preco_unitario'] * self.df['quantidade']

    def obter_total_por_item(self) -> pd.DataFrame:
        return self.df.groupby('nome')['quantidade'].sum().reset_index()

    def obter_receita_por_item(self) -> pd.DataFrame:
        return self.df.groupby('nome')['receita'].sum().reset_index()

    def obter_vendas_por_data(self) -> pd.DataFrame:
        return self.df.groupby(pd.Grouper(key='data', freq='ME'))['quantidade'].sum().reset_index()

    def obter_receita_por_data(self) -> pd.DataFrame:
        return self.df.groupby(pd.Grouper(key='data', freq='ME'))['receita'].sum().reset_index()

    def obter_forma_pagamento(self) -> pd.DataFrame:
        return self.df.groupby('forma_pagamento')['quantidade'].sum().reset_index()

    def obter_preco_medio_por_item(self) -> pd.DataFrame:
        return self.df.groupby('nome')['preco_unitario'].mean().reset_index()