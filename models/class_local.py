from class_ModeloJSON import ModeloJSON, json

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

    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "cidade": self.get_cidade(),
            "irradiacao": self.get_irradiacao()
         }

    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data["id"],
            cidade=data["cidade"],
            irradiacao=data["irradiacao"],
            )

class Locais(ModeloJSON):
    arquivo_json = "locais.json"

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
        
teste = Local(0,"Natal", 5.5525)
Locais.inserir(teste)