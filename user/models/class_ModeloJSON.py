import json



from .class_atendimento import Atendimento
from .class_cliente import Cliente
from .class_item import Item
from .class_kitSolar import KitSolar
from .class_local import Local
from .class_orcamento import Orcamento
from .class_produto import Produto
from .class_Usuarios import Usuario

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
        for obj in cls.lista_obj:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        existente = cls.listar_id(obj.get_id())
        if existente:
            cls.lista_obj.remove(existente)
            cls.lista_obj.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        existente = cls.listar_id(obj.get_id())
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



class Atendimentos(ModeloJSON):
    arquivo_json = "Data/Atendimentos.json"

    @classmethod
    def inserir(cls, atendimento):
        super().inserir(atendimento)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, atendimento):
        super().atualizar(atendimento)

    @classmethod
    def excluir(cls, atendimento):
       super().excluir(atendimento)

    @classmethod
    def abrir(cls):
        
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [Atendimento.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)


class Clientes(ModeloJSON):
    arquivo_json = "Data/clientes.json"

    @classmethod
    def inserir(cls, cliente):
        super().inserir(cliente)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, cliente):
        super().atualizar(cliente)

    @classmethod
    def excluir(cls, cliente):
       super().excluir(cliente)

    @classmethod
    def abrir(cls):
        
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [Cliente.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)


class Itens(ModeloJSON):
    arquivo_json = "Data/Itens.json"

    @classmethod
    def inserir(cls, item):
        super().inserir(item)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, item):
        super().atualizar(item)

    @classmethod
    def excluir(cls, item):
       super().excluir(item)

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


class KitsSolar(ModeloJSON):
    arquivo_json = "Data/KitsSolares.json"

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

class Locais(ModeloJSON):
    arquivo_json = "Data/Locais.json"

    @classmethod
    def inserir(cls, local):
        super().inserir(local)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, local):
        super().atualizar(local)

    @classmethod
    def excluir(cls, local):
        super().excluir(local)

    @classmethod
    def abrir(cls):
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [Local.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
       with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)
        

class Orcamentos(ModeloJSON):
    arquivo_json = "Data/Orçamentos.json"

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


class Produtos(ModeloJSON):
    arquivo_json = "Data/Produtos.json"

    @classmethod
    def inserir(cls, produto):
        super().inserir(produto)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, produto):
        super().atualizar(produto)

    @classmethod
    def excluir(cls, produto):
        super().excluir(produto)

    @classmethod
    def abrir(cls):
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [Produto.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
       with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)


class Usuarios(ModeloJSON):
    arquivo_json = "Data/Usuarios.json"

    @classmethod
    def inserir(cls, Usuario):
        super().inserir(Usuario)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, Usuario):
        super().atualizar(Usuario)

    @classmethod
    def excluir(cls, Usuario):
       super().excluir(Usuario)

    @classmethod
    def abrir(cls):
        
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [Usuario.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)







