import streamlit as st
import os

def main():
    st.set_page_config(page_title="CITAL", page_icon="🚀", layout="wide")

    json_path = os.path.join(os.getcwd(), "data", "cital_data.json")
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Arquivo não encontrado em {json_path}")

if __name__ == "__main__":
    main()