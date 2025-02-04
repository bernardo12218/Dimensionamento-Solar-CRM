from class_ModeloJSON import ModeloJSON
import json

class Item:
    def __init__(self, id, id_Produto, id_Kit, quantidade):
        self.__id = 0
        self.__id_Produto = 0
        self.__id_Kit = 0
        self.__quantidade= 0
     
    
    # sets
        self.set_id(id)
        self.set_id_Produto(id_Produto)
        self.set_id_Kit(id_Kit)
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
    
    def set_id_Kit(self, id_Kit):
        if ((type(id_Kit)  == int) and id_Kit >= 0):
            self.__id_Kit = id_Kit
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

    def get_id_Kit(self):
        return self.__id_Kit

    def get_quantidade(self):
        return self.__quantidade
    
    def __str__(self):
        return f" Id: {self.get_id()} - ID-Produto: {self.get_id_Produto()} - ID-Kit: {self.get_id_Kit()} - Quantidade: {self.get_quantidade()} "

    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "id_Produto": self.get_id_Produto(),
            "id_Kit": self.get_id_Kit(),
            "quantidade": self.get_quantidade()
            
        }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            id_Produto=data["id_Produto"],
            id_Kit=data["id_Kit"],
            quantidade=data["quantidade"]
        )

class Itens(ModeloJSON):
    arquivo_json = "itens.json"

    @classmethod
    def inserir(cls, Item):
        super().inserir(Item)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, Item):
        super().atualizar(Item)

    @classmethod
    def excluir(cls, Item):
       super().excluir(Item)

    @classmethod
    def abrir(cls):
        
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [Item.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)


objeto = Item(0,1,2,30)

Itens.inserir(objeto)
Itens.salvar()

