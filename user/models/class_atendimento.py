# from class_ModeloJSON import ModeloJSON
import json
# 
class Atendimento:
    def __init__(self, id, id_Cliente, potencia, id_Kit_Solar, id_Local, Status, Preco_total):
        self.__id = 0
        self.__id_Cliente = 0
        self.__potencia = 0.0
        self.__id_Kit_Solar = 0
        self.__Preco_total = 0
        self.__id_Local = 0
        self.__Status = 0

        self.set_id(id)
        self.set_id_Cliente(id_Cliente)
        self.set_potencia(potencia)
        self.set_id_Kit_Solar(id_Kit_Solar)
        self.set_Preco_total(Preco_total)
        self.set_id_Local(id_Local)
        self.set_Status(Status)

    def set_id(self, id):
        if type(id) == int and id >= 0:
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def set_id_Cliente(self, id_Cliente):
        if type(id_Cliente) == int and id_Cliente >= 0:
            self.__id_Cliente = id_Cliente
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def set_potencia(self, potencia):
        if type(potencia) == int and potencia >= 0:
            self.__potencia = potencia
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def set_id_Kit_Solar(self, id_Kit_Solar):
        if type(id_Kit_Solar) == int and id_Kit_Solar >= 0:
            self.__id_Kit_Solar = id_Kit_Solar
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def set_Preco_total(self, Preco_total):
        if type(Preco_total) == int and Preco_total >= 0:
            self.__Preco_total = Preco_total
        else:
            raise ValueError("Valor inválido, tente outro valor")


    def set_id_Local(self, id_Local):
        if type(id_Local) == int and id_Local >= 0:
            self.__id_Local = id_Local
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def set_Status(self, Status):
        if type(Status) == int and Status >= 0:
            self.__Status = Status
        else:
            raise ValueError("Valor inválido, tente outro valor")



    


    def get_id(self):
        return self.__id

    def get_id_Cliente(self):
        return self.__id_Cliente

    def get_potencia(self):
        return self.__potencia

    def get_id_Kit_Solar(self):
        return self.__id_Kit_Solar

    def get_Preco_total(self):
        return self.__Preco_total

    def get_id_Local(self):
        return self.__id_Local

    def get_Status(self):
        return self.__Status
    
    def __str__(self):
        return f"Id: {self.get_id()} -id_Cliente: {self.get_id_Cliente()} potencia: {self.get_potencia()} - id_Kit_Solar: {self.get_id_Kit_Solar()} - Preço Total: R${self.get_Preco_total()} - Id_Local: {self.get_id_Local()} - Status: {self.get_Status()}"

    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "id_Cliente": self.get_id_Cliente(),
            "potencia": self.get_potencia(),
            "id_Kit_Solar": self.get_id_Kit_Solar(),
            "Preco_total": self.get_Preco_total(),
            "id_Local": self.get_id_Local(),
            "Status": self.get_Status()
            
        }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            id_Cliente=data["id_Cliente"],
            potencia=data["potencia"],
            id_Kit_Solar=data["id_Kit_Solar"],
            Preco_total=data["Preco_total"],
            id_Local=data["id_Local"],
            Status=data["Status"]
        )

