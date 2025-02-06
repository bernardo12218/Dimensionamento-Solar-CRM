from class_ModeloJSON import ModeloJSON
import json

class Consultor:
    def __init__(self, id, id_descricao, id_preco_total):
        self.__id = 0
        self.__id_descricao = 0
        self.__id_preco_total = 0

        self.set_id(id)
        self.set_id_descricao(id_descricao)
        self.set_id_preco_total(id_preco_total)

    def set_id(self, id):
        if type(id) == int and id >= 0:
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor")

        
    def set__id_descricao(self, id_descricao):
        if type(id_descricao) == int and id_descricao >= 0:
            self.__id_descricao = id_descricao
        else:
            raise ValueError("Valor inválido, tente outro valor")



    def set_id_preco_total(self, id_preco_total):
        if ((type(id_preco_total)  == int) and id_preco_total > 0):
            self.__id_preco_total = id_preco_total
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def get_id(self):
        return self.__id

    def get_id_descricao(self):
        return self.__id_descricao

    def get_id_preco_total(self):
        return self.__id_preco_total



    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "id_descricao": self.get_id_descricao(),
            "id_preco_total": self.get_id_preco_total(),
            
        }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            id_descricao=data["id_descricao"],
            id_preco_total=data["id_preco_total"]
        )

class Consultores(ModeloJSON):
    arquivo_json = "clientes.json"

    @classmethod
    def inserir(cls, consultor):
        super().inserir(consultor)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, consultor):
        super().atualizar(consultor)

    @classmethod
    def excluir(cls, consultor):
       super().excluir(consultor)

    @classmethod
    def abrir(cls):
        
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [Consultor.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)

