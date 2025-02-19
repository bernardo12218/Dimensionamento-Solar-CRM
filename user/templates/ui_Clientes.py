import streamlit as st
from user.view.View import View
import time
import pandas as pd
import json

class UI_Clientes():
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Adicionar", "Atualizar", "Excluir"])

        with tab1:
            UI_Clientes.Listar()
        with tab2:
            UI_Clientes.Adicionar()

    def Listar():
        clientes = View.listar_Cliente()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                st.write(cliente)

    def Adicionar():
        st.header("Cadastra Novo Cliente!")
        nome = st.text_input("Infome o nome: ")
        endereco = st.text_input("Infome o endereço: ")
        cidade = st.text_input("Infome a cidade: ")
        telefone = st.text_input("Infome a telefone: ")
        if st.button("Adicionar Cliente"):
            View.inserir_Cliente(nome,endereco,cidade,telefone)
            st.success("Conta criada com sucesso!")
            time.sleep(2)
            st.rerun()
            UI_Clientes.Adicionar()

