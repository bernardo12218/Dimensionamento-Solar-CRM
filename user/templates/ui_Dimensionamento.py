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
                    st.session_state.cliente_id = op.get_id()
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
                
                kits_solares = UI_Dimensionamento.listar_kits(potencia_kwp)

                opcoes_kits = [f"{kit['descricao']}" for kit in kits_solares]

                kit_selecionado = st.selectbox("Escolha um kit solar:", opcoes_kits)

                kit_detalhes = next((kit for kit in kits_solares if kit["descricao"] == kit_selecionado), None)

                if kit_detalhes:
                    st.write("### Detalhes do Kit Selecionado")
                    st.write(f"**Descrição:** {kit_detalhes['descricao']}")
                    st.write("**Componentes:**")
                    for componente in kit_detalhes["componentes"]:
                        st.write(f"- {componente}")
                    if st.button("Selecionar Kit"):
                        st.session_state.kit_selecionado = kit_detalhes  
                        st.session_state.preco_final = kit_detalhes["preco"]  

                    if "kit_selecionado" in st.session_state:
                        componentes_formatados = " , ".join(st.session_state.kit_selecionado["componentes"])
                        preco_base = st.session_state.kit_selecionado["preco"]  
                        
                        st.write(f"### Kit Solar: {componentes_formatados} - R$ {preco_base:.2f}")
                        preco_Final = st.session_state.kit_selecionado["preco"]
                        preco_Final = st.number_input(
                                "Preço Final R$ ",
                                min_value=st.session_state.kit_selecionado["preco"], 
                                value=st.session_state.preco_final,
                                format="%.2f"
                                )
                                
                        adicao_preco = st.number_input(
                            "Adição no Preço Final (%)",
                            min_value=-100,
                            value=0,
                            format="%d",
                            key="adicao_preco_input"
                        )

                        
                        preco_final_calculado = preco_Final * (1 + adicao_preco / 100)

                        
                        st.write(f"**Preço Final Atualizado:** R$ {preco_final_calculado:.2f}")
                        
                            
                       
                       

                        if st.button("Terminar Dimensionamento"):
                            id_Kit_Selecionado = (kit_detalhes["id"])
                            potencia_Kit = (kit_detalhes["potencia_kit"])
                            id_Local = local.get_id()
                            # st.write(f"{type(potencia_Kit)}")
                            atendimentos = View.listar_Atendimento()
                            for atendimento in atendimentos:
                                if atendimento.get_id_Cliente() == st.session_state.cliente_id:
                                    # st.write(f"Atedimento id-> {atendimento.get_id()} - id_Cliente -> {st.session_state.cliente_id} - Potencia -> {potencia_Kit}, id_kit: {id_Kit_Selecionado} Local {id_Local}, status -> 1 - preco {preco_final_calculado}")

                                    View.atualizar_Atendimento(atendimento.get_id(), st.session_state.cliente_id, potencia_Kit, id_Kit_Selecionado, id_Local, 1, preco_final_calculado)
                                    st.success("Orçamento criado com sucesso!")


                
                
    @staticmethod
    def listar_kits(potencia_kwp):
        kits = View.listar_KitSolar()
        itens = View.listar_Item()
        produtos = View.listar_Produto()
        
        kits_formatados = []
        
        for kit in kits:
            componentes_kitsolar = []
            potencia_kit = 0
            valor_kit = kit.get_valorKit()
            
            for item in itens:
                if item.get_id() in kit.get_idItens():
                    for produto in produtos:
                        if item.get_id_Produto() == produto.get_id():
                            potencia_kit += (item.get_quantidade() * produto.get_potencia()) / 1000  
                            componentes_kitsolar.append(f"{item.get_quantidade()} x {produto.get_tipo()} {produto.get_potencia()}Wp - {produto.get_marca()}")
            
            if componentes_kitsolar:
                kits_formatados.append({
                    "id": kit.get_id(),
                    "preco": kit.get_valorKit(),
                    "descricao": f"Gerador FV {potencia_kit:.2f} kWp - R${valor_kit:.2f}",
                    "componentes": componentes_kitsolar,
                    "potencia_kit": potencia_kit,
                    "valor_kit": valor_kit
                })
        
        return kits_formatados