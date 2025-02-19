from user.view.View import View
from user.templates.ui_Login import UI_Login
import streamlit as st

class Main_UI:
    @staticmethod
    def Main():
        login = UI_Login.main()
        
        if login == "Usuario":
            Main_UI.Main()

    @staticmethod
    def Mudar_Page(pagina):
        st.session_state.page = pagina

Main_UI.Main()

