# from class_ModeloJSON import ModeloJSON, json


class Item:
    def __init__(self, id, id_Produto, id_KitSolar, quantidade):
        self.__id = 0
        self.__id_Produto = 0
        self.__id_KitSolar = 0
        self.__quantidade= 0
     
    
    # sets
        self.set_id(id)
        self.set_id_Produto(id_Produto)
        self.set_id_KitSolar(id_KitSolar)
        self.set_quantidade(quantidade)

    def set_id(self, id):
        if ((type(id)  == int) and id >= 0):
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")
    
    def set_id_Produto(self, id_Produto):
        if ((type(id_Produto)  == int) and id_Produto >= 0):
            self.__id_Produto = id_Produto
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")
    
    def set_id_KitSolar(self, id_KitSolar):
        if ((type(id_KitSolar)  == int) and id_KitSolar >= 0):
            self.__id_KitSolar = id_KitSolar
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")

    def set_quantidade(self,quantidade):
        if (type(quantidade) == int and quantidade >= 0):
            self.__quantidade = quantidade
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")



    # metodos gets
    def get_id(self):
        return self.__id

    def get_id_Produto(self):
        return self.__id_Produto

    def get_id_KitSolar(self):
        return self.__id_KitSolar

    def get_quantidade(self):
        return self.__quantidade
    
    def __str__(self):
        return f" Id: {self.get_id()} - ID-Produto: {self.get_id_Produto()} - ID-kitSolar: {self.get_id_KitSolar()} - Quantidade: {self.get_quantidade()} "

    # def to_dict(self):
       
    #     return {
    #         "id": self.get_id(),
    #         "id_Produto": self.get_id_Produto(),
    #         "id_KitSolar": self.get_id_KitSolar(),
    #         "quantidade": self.get_quantidade()
            
    #     }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            id_Produto=data["id_Produto"],
            id_KitSolar=data["id_KitSolar"],
            quantidade=data["quantidade"]
        )


