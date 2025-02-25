import streamlit as st
from user.view.View import View
import time
import pandas as pd
import json
import re 

class UI_Dimensionamento():
    def main():
        if 'page1' not in st.session_state:
            st.session_state.page1 = 'listar'

        # Page logic
        if st.session_state.page1 == 'listar':
            UI_Dimensionamento.listar_Clientes()
        elif st.session_state.page1 == 'dimensionar':
            UI_Dimensionamento.dimensionar()

    @staticmethod
    def listar_Clientes():
        st.header("Escolha um cliente!")
        clientes = View.listar_Cliente()

        if not clientes:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Selecione o cliente", clientes)

            if op:
                st.write(f"Nome do Cliente: {op.get_nome()} - Telefone: {op.get_telefone()} Cidade -> {op.get_cidade()}")
                if st.button("Dimensionar"):
                    st.session_state.page1 = 'dimensionar'
                    st.session_state.cliente = op
                    st.rerun()

    @staticmethod
    def dimensionar():
        if st.button("Voltar"):
            st.session_state.page1 = 'listar'
            st.rerun()
    
        st.header("Dimensionamento")
        st.header(f"Cliente: {st.session_state.cliente.get_nome()} - Cidade: {st.session_state.cliente.get_cidade()}")
        
        locais = View.listar_Local()
        local = st.selectbox("Selecione o local", locais)

        # ============================= 
        st.write("Digite o consumo médio mensal")

        # Creating columns for each month
        jan, fev, mar, abr, mai, jun = st.columns([1, 1, 1, 1, 1, 1])  
        jul, ago, set, out, nov, dez = st.columns([1, 1, 1, 1, 1, 1]) 

        monthly_values = []

        # Collecting the monthly values
        with jan:
            janeiro = st.number_input("Jan", min_value=0, value=0, format="%d")  
            if janeiro > 0:
                monthly_values.append(janeiro)

        with fev:
            fevereiro = st.number_input("Fev", min_value=0, value=0, format="%d")  
            if fevereiro > 0:
                monthly_values.append(fevereiro)

        with mar:
            marco = st.number_input("Mar", min_value=0, value=0, format="%d")  
            if marco > 0:
                monthly_values.append(marco)

        with abr:
            abril = st.number_input("Abr", min_value=0, value=0, format="%d")  
            if abril > 0:
                monthly_values.append(abril)

        with mai:
            maio = st.number_input("Mai", min_value=0, value=0, format="%d")  
            if maio > 0:
                monthly_values.append(maio)

        with jun:
            junho = st.number_input("Jun", min_value=0, value=0, format="%d")  
            if junho > 0:
                monthly_values.append(junho)

        with jul:
            julho = st.number_input("Jul", min_value=0, value=0, format="%d")  
            if julho > 0:
                monthly_values.append(julho)

        with ago:
            agosto = st.number_input("Ago", min_value=0, value=0, format="%d")  
            if agosto > 0:
                monthly_values.append(agosto)

        with set:
            setembro = st.number_input("Set", min_value=0, value=0, format="%d")  
            if setembro > 0:
                monthly_values.append(setembro)

        with out:
            outubro = st.number_input("Out", min_value=0, value=0, format="%d")  
            if outubro > 0:
                monthly_values.append(outubro)

        with nov:
            novembro = st.number_input("Nov", min_value=0, value=0, format="%d")  
            if novembro > 0:
                monthly_values.append(novembro)

        with dez:
            dezembro = st.number_input("Dez", min_value=0, value=0, format="%d")  
            if dezembro > 0:
                monthly_values.append(dezembro)

       
        adicao = st.number_input("Adição na Média (%)", min_value=-100, value=0, format="%d")  

        if monthly_values:
            consumo = sum(monthly_values) / len(monthly_values)
            consumo_final = consumo + (consumo * (adicao / 100))
            
            st.write(f"Consumo médio mensal do Cliente {st.session_state.cliente.get_nome()}: {consumo_final:.2f} kWh/mês")
            st.write(88 * "=")

            
            if local.get_irradiacao() > 0:
                potencia_kwp = consumo_final / (local.get_irradiacao() * 30 * 0.80)
                st.write(f"Potência necessária do sistema fotovoltaico: {potencia_kwp:.2f} kWp")
                kits = View.listar_KitSolar()
                itens = View.listar_Item()
                produtos = View.listar_Produto()

                
                kitsolar = []
                componentes_kitsolar = []

                    # for item in itens:
                for kit in kits:
                    tamanho_kit = len(kit.get_idItens())
                    for item in itens:
                        for i in range(tamanho_kit):
                            if (kit.get_idItens()[i] == item.get_id()):
                                for produto in produtos:
                                    if item.get_id_Produto() == produto.get_id():

                                        componentes_kitsolar.append(f" Tipo: {produto.get_tipo()} de {produto.get_potencia()}W - Quantidade: {item.get_quantidade()}")
                
                
                st.write(componentes_kitsolar)

                




            else:
                st.write("A irradiância do local não é válida. Não é possível calcular a potência do sistema.")
        else:
            st.write("Nenhum mês foi preenchido.")


