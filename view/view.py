import streamlit as st
import plotly.express as px
import pandas as pd

class VisualizacaoCital:
    def exibir_pagina(
            self,
            total_por_item: pd.DataFrame,
            receita_por_item: pd.DataFrame,
            vendas_por_data: pd.DataFrame,
            receita_por_data: pd.DataFrame,
            forma_pagamento: pd.DataFrame,
            preco_medio_por_item: pd.DataFrame,
            raw_df: pd.DataFrame,
    ) -> None:
        fig = px.bar(
                total_por_item,
                x='nome',
                y='quantidade',
                title='Total de Itens Vendidos por Tipo de Item',
            )
        st.plotly_chart(fig)

        fig = px.bar(
                receita_por_item,
                x='nome',
                y='receita',
                title='Receita Total por Tipo de Item',
            )
        st.plotly_chart(fig)

        fig = px.line(
                vendas_por_data,
                x='data',
                y='quantidade',
                title='Vendas ao Longo do Tempo',
            )
        st.plotly_chart(fig)

        fig = px.line(
            receita_por_data,
                x='data',
                y='receita',
                title='Receita ao Longo do Tempo',
            )
        st.plotly_chart(fig)

        fig = px.pie(
                forma_pagamento,
                names='forma_pagamento',
                values='quantidade',
                title='Forma de Pagamento Utilizada',
            )
        st.plotly_chart(fig)

        fig = px.bar(
                preco_medio_por_item,
                x='nome',
                y='preco_unitario',
                title='Preço Médio por Tipo de Item',
            )
        st.plotly_chart(fig)

        st.write("Dados:")
        st.write(raw_df)