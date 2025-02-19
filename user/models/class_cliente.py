# from class_ModeloJSON import ModeloJSON
import json

class Cliente:
    def __init__(self, id, nome, endereco, cidade, telefone):
        self.__id = 0
        self.__nome = ""
        self.__endereco = ""
        self.__cidade = ""
        self.__telefone = ""

        self.set_id(id)
        self.set_nome(nome)
        self.set_endereco(endereco)
        self.set_cidade(cidade)
        self.set_telefone(telefone)

    def __str__(self):
         return f"Id: {self.get_id()} - Nome: {self.get_nome()} Endereço: {self.get_endereco()} - Cidade: {self.get_cidade()} - Telefone: {self.get_telefone()}"
    def set_id(self, id):
        if type(id) == int and id >= 0:
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def set_nome(self, nome):
            self.__nome = nome


    def set_endereco(self, endereco):
            self.__endereco = endereco

    def set_cidade(self, cidade):
            self.__cidade = cidade

    def set_telefone(self, telefone):
            self.__telefone = telefone

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_cidade(self):
        return self.__cidade

    def get_telefone(self):
        return self.__telefone


    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "endereco": self.get_endereco(),
            "cidade": self.get_cidade(),
            "telefone": self.get_telefone()
            
        }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            nome=data["nome"],
            endereco=data["endereco"],
            cidade=data["cidade"],
            telefone=data["telefone"]
        )

