import streamlit as st
from user.view.View import View
import time
import pandas as pd
import json


class UI_Status:
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["Gestão dos Clientes", "", "Atualizar", "Excluir"])

        with tab1:
            UI_Status.listar_Tabela()
        

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