import streamlit as st
import os
from controller.controller import ControladorCital

def main():
    st.set_page_config(page_title="CITAL", page_icon="🚀", layout="wide")

    json_path = os.path.join(os.getcwd(), "data", "cital_data.json")
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Arquivo não encontrado em {json_path}")

    controlador = ControladorCital(json_path)
    controlador.executar()

if __name__ == "__main__":
    main()