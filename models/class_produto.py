from class_ModeloJSON import ModeloJSON
import json

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

    def to_dict(self):
       
        return {
            "id": self.get_id(),
            "tipo": self.get_tipo(),
            "valor": self.get_valor(),
            "estoque": self.get_estoque(),
            "marca": self.get_marca(),
            "potencia": self.get_potencia()
        }

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

class Produtos(ModeloJSON):
    arquivo_json = "produtos.json"

    @classmethod
    def inserir(cls, produto):
        if not isinstance(produto, Produto):
            raise TypeError("O objeto precisa ser uma instância de Produto")
        super().inserir(produto)

    @classmethod
    def listar(cls):
        return super().listar()

    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)

    @classmethod
    def atualizar(cls, produto):
        if not isinstance(produto, Produto):
            raise TypeError("O objeto precisa ser uma instância de Produto")
        super().atualizar(produto)

    @classmethod
    def excluir(cls, produto):
        if not isinstance(produto, Produto):
            raise TypeError("O objeto precisa ser uma instância de Produto")
        super().excluir(produto)

    @classmethod
    def abrir(cls):
        """ Reescrevendo `abrir()` para criar instâncias de `Produto`. """
        cls.lista_obj = []
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [Produto.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        """ Reescrevendo `salvar()` para converter os objetos `Produto` corretamente. """
        with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)


objeto = Produto(0,"Módulos",1600.50,10,"JA SOLAR", 550)

Produtos.inserir(objeto)
Produtos.salvar()

objeto = Produto(0,"Módulos",1600.50,10,"TRINA", 650)

Produtos.inserir(objeto)
Produtos.salvar()
