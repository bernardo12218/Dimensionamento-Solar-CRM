from class_ModeloJSON import ModeloJSON, json

class KitSolar:
    def __init__(self,id,idItens,quantidade,valorKit):
        self.__id  = 0
        self.__idItens = []
        self.__quantidade = 0
        self.__valorKit = 0.0

        self.set_id(id)
        self.set_idItens(idItens)
        self.set_Quantidade(quantidade)
        self.set_valorKit(valorKit)

    def set_id(self,id):
        if ((type(id)  == int) and id >= 0):
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")

    def set_idItens(self,idItens):
        if ((type(idItens)  == int) and idItens >= 0):
            self.__idItens = (self.get_idItens()).append(idItens)
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")
        
    
    def set_Quantidade(self,quantidade):
        if ((type(id)  == int) and id >= 0):
            self.__quantidade = quantidade
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")

    
    def set_valorKit(self,valorKit):
        if ((type(valorKit)  == float) and valorKit > 0):
            self.__valorKit = valorKit
        else:
            raise ValueError("Valor inválido, tente outro valor positivo")
        
    #metodos gets
    def get_id(self):
        return self.__id
    
    def get_idItens(self):
        return self.__idItens

    def get_Valor(self):
        return self.__Valor
    
    def get_Quantidade(self):
        return self.__quantidade
    
    def __str__(self):
        return f" Id: {self.get_id()} - idItens: {self.get_idItens()} - Valor: R${self.get_Valor()}"

    # def to_dict(self):
       
    #     return {
    #         "id": self.get_id(),
    #         "idItens": self.get_idItens(),
    #         "Valor": self.get_Valor()
    #      }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            idItens=data["idItens"],
            quantidade=data["quantidade"],
            valorKit=data["valorKit"]
            )

class KitsSolar(ModeloJSON):
    arquivo_json = "admin/model/KitsSolares.json"

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


# teste = KitSolar(0,1,50.2)

# KitsSolar.inserir(teste)
teste = KitsSolar.listar()

for i in teste:
    print(teste)