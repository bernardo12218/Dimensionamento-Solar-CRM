from User.models import Cliente, Clientes

class View:
    @staticmethod
    def admin():
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if usuario.get_email() == "admin@gmail.com":
                return None
        
        Usuarios.inserir(Usuario(0, "admin@gmail.com", "1234"))

    @staticmethod
    def inserir_Cliente(nome, endereco, cidade, telefone):
        novo_Cliente = Cliente(0, nome, endereco, cidade, telefone)
        Clientes.inserir(novo_Cliente)

    @staticmethod
    def listar_Cliente():
        return Clientes.listar()
    
    @staticmethod
    def atualizar_Cliente(id, nome, endereco, cidade, telefone):
        novo_Cliente = Cliente(id, nome, endereco, cidade, telefone)
        Clientes.atualizar(novo_Cliente)

    @staticmethod
    def remover_Cliente(id):
        novo_Cliente = Cliente(id, "", "", "", "")
        Clientes.excluir(novo_Cliente)

View.admin()