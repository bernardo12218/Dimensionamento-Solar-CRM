public class TesteItens {
    public static void main(String[] args) {
        // Instancia a classe Itens
        Itens itens = new Itens();

        // Cria alguns itens
        Item item1 = new Item(0, 1, 101, 5); // ID será gerado automaticamente
        Item item2 = new Item(0, 2, 102, 10); // ID será gerado automaticamente

        // Insere os itens
        itens.inserir(item1);
        itens.inserir(item2);

        // Lista todos os itens
        System.out.println("Itens após inserção:");
        for (Item item : itens.listar()) {
            System.out.println(item.get_Id() + " - Produto: " + item.get_Id_Produto() + 
                               ", KitSolar: " + item.get_Id_KitSolar() + 
                               ", Quantidade: " + item.get_Quantidade());
        }

        // Atualiza um item
        Item itemAtualizado = new Item(1, 1, 101, 15); // Atualiza o item com ID 1
        itens.atualizar(itemAtualizado);

        // Lista todos os itens após atualização
        System.out.println("\nItens após atualização:");
        for (Item item : itens.listar()) {
            System.out.println(item.get_Id() + " - Produto: " + item.get_Id_Produto() + 
                               ", KitSolar: " + item.get_Id_KitSolar() + 
                               ", Quantidade: " + item.get_Quantidade());
        }

        // Exclui um item
        Item itemParaExcluir = itens.listarId(2); // Exclui o item com ID 2
        if (itemParaExcluir != null) {
            itens.excluir(itemParaExcluir);
        }

        // Lista todos os itens após exclusão
        System.out.println("\nItens após exclusão:");
        for (Item item : itens.listar()) {
            System.out.println(item.get_Id() + " - Produto: " + item.get_Id_Produto() + 
                               ", KitSolar: " + item.get_Id_KitSolar() + 
                               ", Quantidade: " + item.get_Quantidade());
        }
    }
}