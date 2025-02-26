from user.view.View import View
from user.templates.ui_Login import UI_Login
from user.templates.ui_Clientes import UI_Clientes
from user.templates.ui_Status import UI_Status
from user.templates.ui_Dimensionamento import UI_Dimensionamento

import streamlit as st

class Main_UI:
    @staticmethod
    def Main():
        Main_UI.Inicio()
        # UI_Clientes.main()


    @staticmethod
    def login():
        login = UI_Login.main()
        
        if login == "Usuario":
            Main_UI.Mudar_Page('usuario')
            st.rerun()

    @staticmethod
    def Inicio():
        if 'page' not in st.session_state:
            st.session_state.page = 'home'
        
        if st.session_state.page == 'home':
            st.write("Página Inicial")
            Main_UI.login()
            # UI_Dimensionamento.main()
            # UI_Status.main()


        elif st.session_state.page == 'usuario':
            Main_UI.Usuario_Tela()

    
    @staticmethod
    def Mudar_Page(pagina):
        st.session_state.page = pagina

    def Usuario_Tela():
        op = st.sidebar.selectbox("Menu", ["CRM","Cliente", "Orçamento", "Fechar Pedido", "Ver Meus Pedidos", "Sair"])
        if op == "CRM":
                UI_Status.main()
        if op == "Cliente":
                UI_Clientes.main()
        if op == "Orçamento":
                UI_Dimensionamento.main()
        if op == "Sair":
                st.session_state.page = 'home'
                st.rerun()
                Main_UI.Main()


        


Main_UI.Main()

