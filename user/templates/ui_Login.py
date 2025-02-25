import streamlit as st
from user.view.View import View
import time

class UI_Login:
    @staticmethod
    def main():
        
        # st.write("TEstando")
        # testes = View.listar_Cliente()
        # for teste in testes:
        #     st.write(teste)
        st.header("Conecte-se")
        email = st.text_input("Digite o email: ")
        senha = st.text_input("Digite o senha: ",type = "password")
    
        resultado = View.login(email,senha)
           
        if st.button("Entrar"):
            if email and senha:
                if resultado is None:
                    st.error("Email ou senha invalidos")
                else:
                    return "Usuario"

