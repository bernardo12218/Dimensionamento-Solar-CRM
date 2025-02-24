import streamlit as st
from user.view.View import View
import time
import pandas as pd
import json
import re  # Importação para validação de regex

class UI_Clientes():
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Adicionar", "Atualizar", "Excluir"])

        with tab1:
            UI_Clientes.Listar()
        with tab2:
            UI_Clientes.Adicionar()

        with tab3:
            UI_Clientes.Atualizar()

    def Listar():
        clientes = View.listar_Cliente()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                st.write(cliente)

    def Adicionar():
        st.header("Cadastrar Novo Cliente")
        nome = st.text_input("Informe o nome:")
        endereco = st.text_input("Informe o endereço:")
        cidade = st.text_input("Informe o cidade:")
        telefone = st.text_input("Informe o telefone:")

        
        def validar_nome(nome):
            if len(nome) < 3:
                return 0
            else:
                return 1
        def validar_endereco(endereço):
            if len(endereço) < 6:
                return 0
            else:
                return 1
       
        
        def validar_telefone(telefone):
            return bool(re.fullmatch(r"\d{8,15}", telefone))

        if st.button("Adicionar Cliente"):
            
            if not nome or not telefone or not cidade or not telefone:
                st.warning("Preencha todos os campos!")
                return None
            
            
            if validar_nome(nome) == 0:
                st.warning("Nome inválido! Use no mínimo de 3 caracteres.")
                return None

            if validar_endereco(endereco) == 0:
                st.warning("Endeço inválido! Use no mínimo de 3 caracteres.")
                return None

            if validar_nome(cidade) == 0:
                st.warning("Nome inválido! Use no mínimo de 3 caracteres.")
                return None

            if not validar_telefone(telefone):
                st.warning("Telefone inválido! Use apenas números e entre 8 e 15 dígitos.")
                return None
                       
            clientes = View.listar_Cliente()
            for cliente in clientes: 
                if cliente.get_nome() == nome and cliente.get_telefone() == telefone:
                    st.warning("Cliente já existente.")
                    return None

           
            View.inserir_Cliente(nome, endereco, cidade, telefone)
            st.success("Cliente cadastrado com sucesso!")
            time.sleep(2)
            st.rerun()


    def Atualizar():
        st.header("Atualizar Cliente!")
        clientes = View.listar_Cliente()

        clientes = clientes[1:]
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Selecione o cliente", clientes)
            nome = st.text_input("Informe o nome: ", op.get_nome())
            endereco = st.text_input("Informe o endereço: ", op.get_endereco())
            telefone = st.text_input("Informe o email: ", op.get_telefone())
            cidade = st.text_input("Informe o cidade: ", op.get_cidade())
            def validar_nome(nome):
                if len(nome) < 3:
                    return 0
                else:
                    return 1
            def validar_endereco(endereço):
                if len(endereço) < 6:
                    return 0
                else:
                    return 1
       
        
            def validar_telefone(telefone):
                return bool(re.fullmatch(r"\d{8,15}", telefone))

            if st.button("Atualizar"):
                if not nome or not telefone or not cidade or not telefone:
                    st.warning("Preencha todos os campos!")
                    return None
            
            
                if validar_nome(nome) == 0:
                    st.warning("Nome inválido! Use no mínimo de 3 caracteres.")
                    return None

                if validar_endereco(endereco) == 0:
                    st.warning("Endeço inválido! Use no mínimo de 3 caracteres.")
                    return None

                if validar_nome(cidade) == 0:
                    st.warning("Nome inválido! Use no mínimo de 3 caracteres.")
                    return None

                if not validar_telefone(telefone):
                    st.warning("Telefone inválido! Use apenas números e entre 8 e 15 dígitos.")
                    return None

                clientes = View.listar_Cliente()
                for cliente in clientes: 
                    if cliente.get_nome() == nome and cliente.get_telefone() == telefone:
                        st.warning("Cliente já existente.")
                        return None

                View.atualizar_Cliente(op.get_id(), nome, endereco, cidade, telefone)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
