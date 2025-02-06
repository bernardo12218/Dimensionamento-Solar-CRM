from class_ModeloJSON import ModeloJSON
import json

class Orcamento:
    def __init__(self, id, id_kitSolar, descricao, preco_total):
        self.__id = 0
        self.__id_kitSolar = 0
        self.__descricao = ""
        self.__preco_total = 0.0

        self.set_id(id)
        self.set_id_kitSolar(id_kitSolar)
        self.set_descricao(descricao)
        self.set_preco_total(preco_total)

    def set_id(self, id):
        if type(id) == int and id >= 0:
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def set_id_kitSolar(self, id_kitSolar):
        if type(id) == int and id >= 0:
            self.__id_kitSolar = id_kitSolar
        else:
            raise ValueError("Valor inválido, tente outro valor")
        
    def set__descricao(self, descricao):
        return self.__descricao


    def set_preco_total(self, preco_total):
        if ((type(preco_total)  == float) and preco_total > 0):
            self.__preco_total = preco_total
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def get_id(self):
        return self.__id

    def get_id_kitSolar(self):
        return self.__id_kitSolar

    def get_descricao(self):
        return self.__descricao

    def get_preco_total(self):
        return self.__preco_total



    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "id_kitSolar": self.get_id_kitSolar(),
            "descricao": self.get_descricao(),
            "preco_total": self.get_preco_total(),
            
        }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            id_kitSolar=data["id_kitSolar"],
            descricao=data["descricao"],
            preco_total=data["preco_total"],
        )

class Orcamentos(ModeloJSON):
    arquivo_json = "clientes.json"

    @classmethod
    def inserir(cls, orcamento):
        super().inserir(orcamento)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, orcamento):
        super().atualizar(orcamento)

    @classmethod
    def excluir(cls, orcamento):
       super().excluir(orcamento)

    @classmethod
    def abrir(cls):
        
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [Orcamento.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)

