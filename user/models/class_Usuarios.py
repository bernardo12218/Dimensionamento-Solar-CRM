# from class_ModeloJSON import ModeloJSON
import json

class Usuario:
    def __init__(self, id, email, senha):
        self.__id = 0
        self.__email = ""
        self.__senha = ""
   

        self.set_id(id)
        self.set_email(email)
        self.set_senha(senha)
     

    def __str__(self):
         return f"Id: {self.get_id()} - Email: {self.get_email()} - senha: {self.get_senha()}"
    def set_id(self, id):
        if type(id) == int and id >= 0:
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def set_email(self, email):
            self.__email = email


    def set_senha(self, senha):
            self.__senha = senha

  
    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

   


    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "email": self.get_email(),
            "senha": self.get_senha()
            
        }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            email=data["email"],
            senha=data["senha"]
        )


