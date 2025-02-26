from user.models import Cliente, Clientes, Usuario, Usuarios, Atendimento, Atendimentos, Local, Locais, KitSolar, KitsSolar, Item, Itens, Produto, Produtos


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
                print
                return "Usuario"

                
           
    # =========== Fim-Verificar_Login ================

    @staticmethod
    def inserir_Cliente(nome, endereco, cidade, telefone):
        novo_Cliente = Cliente(0, nome, endereco, cidade, telefone)
        
        Clientes.inserir(novo_Cliente)
        clientes =  Clientes.listar()
        for cliente in clientes:
            if cliente.get_nome() == nome and cliente.get_endereco() ==  endereco and cliente.get_cidade() == cidade and cliente.get_telefone() == telefone:
                novo_Atendimento = Atendimento(0,cliente.get_id(),0,0,0,0,0)
                Atendimentos.inserir(novo_Atendimento)


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
        # id, id_Cliente, potencia, id_Kit_Solar, id_Local, Status, Preco_total
        atendimentos = View.listar_Atendimento()
        print(atendimentos)
        for atendimento in atendimentos:
            if id == atendimento.get_id_Cliente():
                # print(f"id-> {atendimento.get_id()} id_Cliente -> {atendimento.get_id_Cliente()}")
                novo_Atendimento = Atendimento(atendimento.get_id(),0,0,0,0,0,0)
                Atendimentos.excluir(novo_Atendimento)

    # =============================================
    @staticmethod
    def listar_Atendimento():
        return Atendimentos.listar()

    @staticmethod
    def atualizar_Atendimento(id, id_Cliente, potencia, id_Kit_Solar, id_Local, Status, Preco_total):
        novo_Atendimento = Atendimento(id, id_Cliente, potencia, id_Kit_Solar, id_Local, Status, Preco_total)
        Atendimentos.atualizar(novo_Atendimento)
    
    @staticmethod
    def listar_Local():
        return Locais.listar()
    
    @staticmethod
    def listar_KitSolar():
        return KitsSolar.listar()
    
    @staticmethod
    def listar_Item():
        return Itens.listar()
    
    @staticmethod
    def listar_Produto():
        return Produtos.listar()

