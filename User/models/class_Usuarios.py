from class_ModeloJSON import ModeloJSON
import json

class Usuario:
    def __init__(self, id, email, senha):
        self.__id = 0
        self.__email = ""
        self.__senha = ""
        self.__cidade = ""
        self.__telefone = ""

        self.set_id(id)
        self.set_email(email)
        self.set_senha(senha)
     

    def set_id(self, id):
        if type(id) == int and id >= 0:
            self.__id = id
        else:
            raise ValueError("Valor inválido, tente outro valor")

    def set_email(self, email):
            self.__email = email


    def set_senha(self, senha):
            self.__senha = senha

  
    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

   


    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "email": self.get_email(),
            "senha": self.get_senha()
            
        }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            email=data["email"],
            senha=data["senha"]
        )

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


email = "Asaph Arruda"
senha = "Rua gameleira 361 - Nova Parnamirim"


novo_Usuario = Usuario(0,email,senha)

Usuarios.inserir(novo_Usuario)