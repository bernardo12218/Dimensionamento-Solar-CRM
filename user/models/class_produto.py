# from class_ModeloJSON import ModeloJSON, json


class Produto:
    def __init__(self, id, tipo, valor, estoque, marca, potencia):
        self.__id = 0
        self.__tipo = ""
        self.__valor = 0.0
        self.__estoque = 0
        self.__marca = ""
        self.__potencia = 0        
    
    # sets
        self.set_id(id)
        self.set_tipo(tipo)
        self.set_valor(valor)
        self.set_estoque(estoque)
        self.set_marca(marca)
        self.set_potencia(potencia)

    def set_id(self, id):
        if ((type(id)  == int) and id >= 0):
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")
    
    def set_tipo(self, tipo):
        self.__tipo = tipo
    
    def set_valor(self, valor):
        if (type(valor) == float and valor > 0):
            self.__valor = valor
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")

    def set_estoque(self,estoque):
        if (type(estoque) == int and estoque >= 0):
            self.__estoque = estoque
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")


    def set_marca(self, marca):
        self.__marca = marca
    
    def set_potencia(self,potencia):
        if (type(potencia) == int and potencia > 0):
            self.__potencia = potencia
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")


    # metodos gets
    def get_id(self):
        return self.__id

    def get_tipo(self):
        return self.__tipo

    def get_valor(self):
        return self.__valor

    def get_estoque(self):
        return self.__estoque

    def get_marca(self):
        return self.__marca

    def get_potencia(self):
        return self.__potencia
    
    def __str__(self):
        return f" Id: {self.get_id()} - Tipo: {self.get_tipo()} - Valor: R${self.get_valor()} - Estoque: {self.get_estoque()} - Marca: {self.get_marca()} - Potencia: {self.get_potencia()} Watts"

    #def to_dict(self):
       
    #    return {
    #       "id": self.get_id(),
    #        "tipo": self.get_tipo(),
    #        "valor": self.get_valor(),
    #        "estoque": self.get_estoque(),
    #        "marca": self.get_marca(),
    #        "potencia": self.get_potencia()
     #   }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            tipo=data["tipo"],
            valor=data["valor"],
            estoque=data["estoque"],
            marca=data["marca"],
            potencia=data["potencia"]
        )


