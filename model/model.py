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

    def obter_total_por_item(self) -> pd.DataFrame:
        return self.df.groupby('nome')['quantidade'].sum().reset_index()