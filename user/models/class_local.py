# from class_ModeloJSON import ModeloJSON, json

class Local:
    def __init__(self,id,cidade,irradiacao) -> None:
        self.__id = 0
        self.__cidade = ""
        self.__irradiacao = 0.0

        self.set_id(id)
        self.set_cidade(cidade)
        self.set_irradiacao(irradiacao)
    
    
    #metodos sets
    def set_id(self,id):
        if ((type(id)  == int) and id >= 0):
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")


    def set_cidade(self,cidade):
        self.__cidade = cidade
    
    def set_irradiacao(self,irradiacao):
        if ((type(irradiacao)  == float) and irradiacao > 0):
            self.__irradiacao = irradiacao
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")

    #metodos gets
    def get_id(self):
        return self.__id

    def get_cidade(self):
        return self.__cidade

    def get_irradiacao(self):
        return self.__irradiacao

    def __str__(self):
        return f" Id: {self.get_id()} - Cidade: {self.get_cidade()} - Irradiacao: {self.get_irradiacao()}"

    #def to_dict(self):
       
       # return {
        #    "id": self.get_id(),
        #    "cidade": self.get_cidade(),
       #     "irradiacao": self.get_irradiacao()
       #  }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            cidade=data["cidade"],
            irradiacao=data["irradiacao"],
            )

