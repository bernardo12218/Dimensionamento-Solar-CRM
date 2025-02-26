import streamlit as st
from user.view.View import View
import time
import pandas as pd
import json


class UI_Status:
    def main():
        tab1, tab2 = st.tabs(["Gestão dos Clientes", "Atualizar"])

        with tab1:
            UI_Status.listar_Tabela()
        with tab2:
            UI_Status.atualizar_Status()
        

    def listar_Tabela():
        atendimentos = View.listar_Atendimento()
        aguardando_Orcamento = [a for a in atendimentos if a.get_Status() == 0]
        orcamento_Realizado =  [a for a in atendimentos if a.get_Status() == 1]
        orcamento_Enviado =    [a for a in atendimentos if a.get_Status() == 2]
        esperando_Resposta =   [a for a in atendimentos if a.get_Status() == 3]
        cliente_Fechado =      [a for a in atendimentos if a.get_Status() == 4]
        cliente_Congelado =    [a for a in atendimentos if a.get_Status() == 5]
        cliente_Analise =      [a for a in atendimentos if a.get_Status() == 6]
           
        aguardando_Orcamento_data = UI_Status.Organizar(aguardando_Orcamento)
        orcamento_Realizado_data = UI_Status.Organizar(orcamento_Realizado)
        orcamento_Enviado_data = UI_Status.Organizar(orcamento_Enviado)
        esperando_Resposta_data = UI_Status.Organizar(esperando_Resposta)
        cliente_Fechado_data = UI_Status.Organizar(cliente_Fechado)
        cliente_Congelado_data = UI_Status.Organizar(cliente_Congelado)
        cliente_Analise_data = UI_Status.Organizar(cliente_Analise)

       
        max_len = max(len(aguardando_Orcamento_data), len(orcamento_Realizado_data), len(orcamento_Enviado_data), len(esperando_Resposta_data), len(cliente_Fechado_data), len(cliente_Congelado_data), len(cliente_Analise_data))
        aguardando_Orcamento_data += [""] * (max_len - len(aguardando_Orcamento_data))
        orcamento_Realizado_data += [""] * (max_len - len(orcamento_Realizado_data))
        orcamento_Enviado_data += [""] * (max_len - len(orcamento_Enviado_data))
        esperando_Resposta_data += [""] * (max_len - len(esperando_Resposta_data))
        cliente_Fechado_data += [""] * (max_len - len(cliente_Fechado_data))
        cliente_Congelado_data += [""] * (max_len - len(cliente_Congelado_data))
        cliente_Analise_data += [""] * (max_len - len(cliente_Analise_data))
       
        
        
        df = pd.DataFrame({
            "Aguardando Orçamento": aguardando_Orcamento_data,
            "Orçamento Realizado": orcamento_Realizado_data,
            "Orçamento Enviado": orcamento_Enviado_data,
            "Esperando Resposta": esperando_Resposta_data,
            "Cliente Analisando": cliente_Analise_data,
            "Cliente Congelado": cliente_Congelado_data,
            "Cliente Fechado": cliente_Fechado_data

        })

        
        st.write("Tabela de Atendimentos")
        st.table(df)
        # st.dataframe(df, use_container_width=True)

        

    @staticmethod
    def Organizar(array):
        clientes = View.listar_Cliente()
        array_novo = []
        for atendimento in array: 
            for cliente in clientes:
                if (cliente.get_id() == atendimento.get_id_Cliente()):
                    array_novo.append(cliente.get_nome())

        return array_novo

    
    @staticmethod
    def atualizar_Status():
        atendimentos = View.listar_Atendimento()
        clientes = View.listar_Cliente()

        if len(atendimentos) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            
            op = st.selectbox("Selecione o cliente", atendimentos)
         
            
            for cliente in clientes:
                if cliente.get_id() == op.get_id_Cliente():
                    nome = cliente.get_nome()

                    status = op.get_Status()
                    
            if status == 0:
                status = "Esperando Orçamento"
            elif status == 1:
                status = "Orçamento Realizado"
            elif status == 2:
                status = "Orçamento Enviado"
            elif status == 3:
                status = "Esperando Resposta"
            elif status == 4:
                status = "Cliente Analisando"
            elif status == 5:
                status = "Cliente Congelado"
            elif status == 6:
                status = "Cliente Fechado"

            kits = View.listar_KitSolar()
            itens = View.listar_Item()
            produtos = View.listar_Produto()

            produtosKit = []
            componentes_kitsolar = []

            for kit in kits:
                if kit.get_id() == op.get_id_Kit_Solar():
                    kit = kit
                    break
                kit = None

            # st.write(kit)
            # st.write(op.get_id_Kit_Solar())

            if kit:     
                tamanho_kit = len(kit.get_idItens())
                for item in itens:
                    for i in range(tamanho_kit):
                        if (kit.get_idItens()[i] == item.get_id()):
                            for produto in produtos:
                                if item.get_id_Produto() == produto.get_id():
                                    if len(componentes_kitsolar)== 0:
                                        componentes_kitsolar.append(f"Gerador FV {(item.get_quantidade() * produto.get_potencia()) / 1000 } Kwp")

                                    produtosKit.append(f"{produto.get_tipo()} de {produto.get_potencia() }W x {item.get_quantidade()}")


            

            # st.write(f"Cliente: {nome} - Status: **{status}**")
            st.write(f"### Nome: {nome} - {status}")
            st.write(f"### Potencia do Sistema: {op.get_potencia()}Kwp")
            for componente_kitsolar in componentes_kitsolar:
                st.write(f"###### {componente_kitsolar}")  

            for componente_kitsolar in produtosKit:
                st.write(f"###### {componente_kitsolar}")       

            st.write(f"### Preço Total: R${op.get_Preco_total()}")

            operacoes = ["Orçamento Enviado", "Esperando Resposta","Cliente Analisando", "Cliente Congelado", "Cliente Fechado"]
            
            for operacao in operacoes:
                if operacao == status:
                    operaca_status = status
                        
            
           

            if produtosKit:
                if status in operacoes:
                    operacoes.remove(status)

            
                st.write("Operações Disponíveis para Atualização:")
                                
                nova_operacao = st.selectbox("Escolha uma nova operação", operacoes)

                
                if st.button("Confirmar Atualização"):
                    match nova_operacao:
                        case "Orçamento Enviado":
                            status = 2
                        case "Esperando Resposta":
                            status = 3
                        case "Cliente Analisando":
                            status = 6
                        case "Cliente Congelado":
                            status = 5
                        case "Cliente Fechado":
                            status = 4
                    # View.atualizar_Atendimento(atendimento.get_id(), st.session_state.cliente_id, potencia_Kit, id_Kit_Selecionado, id_Local, 1, preco_final_calculado)
                                    # st.success("Orçamento criado com sucesso!")
                    View.atualizar_Atendimento(op.get_id(),op.get_id_Cliente(),op.get_potencia(),op.get_id_Kit_Solar(),op.get_id_Local(),status,op.get_Preco_total())
                

                    
                    st.success(f"Status atualizado para: {nova_operacao}")
                    time.sleep(2)
                    st.rerun()

        
            