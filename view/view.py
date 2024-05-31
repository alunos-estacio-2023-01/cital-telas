import streamlit as st
import plotly.express as px
import pandas as pd

class VisualizacaoCital:
    def exibir_pagina(
            self,
            total_por_item: pd.DataFrame,
            receita_por_item: pd.DataFrame,
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