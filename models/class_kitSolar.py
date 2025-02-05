from class_ModeloJSON import ModeloJSON, json

class KitSolar:
    def __init__(self,id,id_Item,valor):
        self.__id  = 0
        self.__id_Item = 0
        self.__Valor = 0.0

        self.set_id(id)
        self.set_id_Item(id_Item)
        self.set_Valor(valor)

    def set_id(self,id):
        if ((type(id)  == int) and id >= 0):
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")

    def set_id_Item(self,id_Item):
        if ((type(id_Item)  == int) and id_Item >= 0):
            self.__id_Item = id_Item
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")

    
    def set_Valor(self,valor):
        if ((type(valor)  == float) and valor > 0):
            self.__Valor = valor
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")
        
    #metodos gets
    def get_id(self):
        return self.__id
    
    def get_id_Item(self):
        return self.__id_Item

    def get_Valor(self):
        return self.__Valor

    
    def __str__(self):
        return f" Id: {self.get_id()} - id_Item: {self.get_id_Item()} - Valor: R${self.get_Valor()}"

    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "id_Item": self.get_id_Item(),
            "Valor": self.get_Valor()
         }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            id_Item=data["id_Item"],
            valor=data["Valor"]
            )

class KitsSolar(ModeloJSON):
    arquivo_json = "KitsSolar.json"

    @classmethod
    def inserir(cls, kitSolar):
        super().inserir(kitSolar)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, kitSolar):
        super().atualizar(kitSolar)

    @classmethod
    def excluir(cls, kitSolar):
        super().excluir(kitSolar)

    @classmethod
    def abrir(cls):
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [KitSolar.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
       with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)


teste = KitSolar(0,1,50.2)

KitsSolar.inserir(teste)