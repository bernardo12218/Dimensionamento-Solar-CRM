from user.models import Cliente, Clientes, Usuario, Usuarios


class View:

    # =========== CADASTRAR ADMIN ================
    @staticmethod
    def admin():
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if usuario.get_email() == "admin@gmail.com":
                return None
        
        Usuarios.inserir(Usuario(0, "admin@gmail.com", "1234"))
    # =========== Fim-CADASTRAR ADMIN ================

    # =========== CADASTRAR USUARIO ================
    @staticmethod
    def user():
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if usuario.get_email() == "empresa@gmail.com":
                return None
        
        Usuarios.inserir(Usuario(0, "empresa@gmail.com", "1234"))

    # =========== Fim-CADASTRAR USUARIO ================

    # =========== Verificar_Login ================
    @staticmethod
    def login(email,senha):
        usarios = Usuarios.listar()
        for usuario in usarios:
            if "empresa@gmail.com" == email and "1234" == senha:
                return "Usuario"
                
           
    # =========== Fim-Verificar_Login ================

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

