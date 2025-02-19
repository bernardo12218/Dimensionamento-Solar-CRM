import json

class ModeloJSON:
    lista_obj = []
    arquivo_json = "base.json" 

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.lista_obj:
            if x.get_id() > id:  
                id = x.get_id()

        obj.set_id(id + 1)
        cls.lista_obj.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.lista_obj

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.lista_obj:
            if x.id == id:
                return x
        return None

    @classmethod
    def atualizar(cls, obj):
        existente = cls.listar_id(obj.id)
        if existente:
            cls.lista_obj.remove(existente)
            cls.lista_obj.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        existente = cls.listar_id(obj.id)
        if existente:
            cls.lista_obj.remove(existente)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open(cls.arquivo_json, "w") as arquivo:
            json.dump([vars(obj) for obj in cls.lista_obj], arquivo)

    @classmethod
    def abrir(cls):
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [cls(**obj) for obj in arquivo_json]  
        except FileNotFoundError:
            pass