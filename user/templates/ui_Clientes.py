import streamlit as st
from user.view.View import View
import time
import pandas as pd
import json
import re  # Importação para validação de regex

class UI_Clientes():
    def main():
        if st.session_state["Dimensionar"] == True:
            UI_Clientes.Dimensionar()
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Adicionar", "Atualizar", "Excluir"])


        with tab1:
            UI_Clientes.Listar()
        with tab2:
            UI_Clientes.Adicionar()

        with tab3:
            UI_Clientes.Atualizar()

        with tab4:
            UI_Clientes.Excluir()

    def Listar():
        clientes = View.listar_Cliente()
        


        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            clientes = View.listar_Cliente()

            nomes = []
            for nome in clientes:
                nomes.append(nome.get_nome())
            
            enderecos = []
            for endereco in clientes:
                enderecos.append(endereco.get_endereco())
            

            cidades = []
            for cidade in clientes:
                cidades.append(cidade.get_cidade())

            telefones = []
            for telefone in clientes:
                telefones.append(telefone.get_telefone())

            df = pd.DataFrame({
            "Nome": nomes,
            "Endereço": enderecos,
            "Cidade": cidades,
            "Telefone": telefones
       
        })

        
            st.write("Tabela de Atendimentos")
            st.table(df)


    def Adicionar():
        st.header("Cadastrar Novo Cliente")
        nome = st.text_input("Informe o nome:")
        endereco = st.text_input("Informe o endereço:")
        cidade = st.text_input("Informe o cidade:")
        telefone = st.text_input("Informe o telefone:")

        if "cliente_cadastrado" not in st.session_state:
            st.session_state["cliente_cadastrado"] = False  # Inicializa o estado

        def validar_nome(nome):
            return len(nome) >= 3

        def validar_endereco(endereco):
            return len(endereco) >= 6

        def validar_telefone(telefone):
            return bool(re.fullmatch(r"\d{8,15}", telefone))

        col1, col2 = st.columns([1, 1])  # Cria duas colunas iguais

        with col1:
            if st.button("Adicionar Cliente"):
                if not nome or not telefone or not cidade or not endereco:
                    st.warning("Preencha todos os campos!")
                    return None

                if not validar_nome(nome):
                    st.warning("Nome inválido! Use no mínimo 3 caracteres.")
                    return None

                if not validar_endereco(endereco):
                    st.warning("Endereço inválido! Use no mínimo 6 caracteres.")
                    return None

                if not validar_nome(cidade):
                    st.warning("Cidade inválida! Use no mínimo 3 caracteres.")
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

                # Ativa o botão "Dimensionar"
                st.session_state["cliente_cadastrado"] = True
                st.rerun()

        with col2:
            if st.session_state["cliente_cadastrado"]:
                if st.button("Dimensionar"):
                    st.session_state["Dimensionar"] = True
                    st.info("Aqui você pode implementar a funcionalidade de dimensionamento.")
                    return UI_Clientes.main()

    def Atualizar():
        st.header("Atualizar Cliente!")
        clientes = View.listar_Cliente()

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

    def Excluir():
        st.header("Remover Cliente!")
        clientes = View.listar_Cliente()

        
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de cliente", clientes)
            if st.button("Excluir"):
                View.remover_Cliente(op.get_id())
                st.success("Cliente excluido com sucesso!")
                time.sleep(2)
                st.rerun()


    def Dimensionar():
        st.write("asfoahfd")