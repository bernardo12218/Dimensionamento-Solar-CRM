package admin.Models.src;

import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Produtos produtos = new Produtos(); 
        Itens itens = new Itens();
        Scanner scanner = new Scanner(System.in); 

        int opcao;

        do {
            System.out.println("\n--- Menu Principal ---");
            System.out.println("1. Gerenciar Produtos");
            System.out.println("2. Gerenciar Itens");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine(); 

            switch (opcao) {
                case 1:
                    gerenciarProdutos(produtos, scanner); 
                    break;

                case 2:
                    MontarItens(produtos, itens,scanner );
                    break;

                case 0:
                    System.out.println("Saindo...");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        } while (opcao != 0);

        scanner.close(); // Fechar o scanner ao final
    }

    public static void gerenciarProdutos(Produtos produtos, Scanner scanner) {
        int operacao;

        do {
            System.out.println("\n--- Menu de Produtos ---");
            System.out.println("1. Adicionar Produto");
            System.out.println("2. Listar Produtos");
            System.out.println("3. Atualizar Produto");
            System.out.println("4. Excluir Produto");
            System.out.println("0. Voltar");
            System.out.print("Escolha uma opção: ");
            operacao = scanner.nextInt();
            scanner.nextLine(); // Consumir a nova linha

            switch (operacao) {
                case 1:
                    System.out.println("\n--- ** Inserindo Produto ** ---");
                    System.out.print("Digite o tipo do Produto: ");
                    String tipoProduto = scanner.nextLine();
                    System.out.print("Digite o valor do Produto: R$");
                    float valor = scanner.nextFloat();
                    System.out.print("Digite o estoque do Produto: ");
                    int estoque = scanner.nextInt();
                    scanner.nextLine(); // Consumir a nova linha
                    System.out.print("Digite a marca do Produto: ");
                    String marca = scanner.nextLine();
                    System.out.print("Digite a potência do Produto (em Watts): ");
                    int potencia = scanner.nextInt();
                    scanner.nextLine(); // Consumir a nova linha

                    produtos.inserir(new Produto(0, tipoProduto, valor, estoque, marca, potencia));
                    System.out.println("Produto adicionado com sucesso!");
                    break;

                case 2:
                    System.out.println("\n--- ** Listando Produtos ** ---");
                    for (Produto produto : produtos.listar()) {
                        System.out.println(produto);
                    }
                    break;

                case 3:
                    System.out.println("\n--- ** Atualizando Produto ** ---");
                    System.out.print("Digite o ID do produto que deseja atualizar: ");
                    int idAtualizar = scanner.nextInt();
                    scanner.nextLine(); // Consumir a nova linha

                    Produto produtoAtualizado = produtos.listarId(idAtualizar);
                    if (produtoAtualizado != null) {
                        System.out.print("Digite o novo tipo do Produto: ");
                        String novoTipo = scanner.nextLine();
                        System.out.print("Digite o novo valor do Produto: R$");
                        float novoValor = scanner.nextFloat();
                        System.out.print("Digite o novo estoque do Produto: ");
                        int novoEstoque = scanner.nextInt();
                        scanner.nextLine(); // Consumir a nova linha
                        System.out.print("Digite a nova marca do Produto: ");
                        String novaMarca = scanner.nextLine();
                        System.out.print("Digite a nova potência do Produto (em Watts): ");
                        int novaPotencia = scanner.nextInt();
                        scanner.nextLine(); // Consumir a nova linha

                        produtoAtualizado.setTipo(novoTipo);
                        produtoAtualizado.setValor(novoValor);
                        produtoAtualizado.setEstoque(novoEstoque);
                        produtoAtualizado.setMarca(novaMarca);
                        produtoAtualizado.setPotencia(novaPotencia);

                        produtos.atualizar(produtoAtualizado);
                        System.out.println("Produto atualizado com sucesso!");
                    } else {
                        System.out.println("Produto não encontrado.");
                    }
                    break;

                case 4:
                    System.out.println("\n--- ** Excluindo Produto ** ---");
                    System.out.print("Digite o ID do produto que deseja excluir: ");
                    int idExcluir = scanner.nextInt();
                    scanner.nextLine(); // Consumir a nova linha

                    Produto produtoExcluir = produtos.listarId(idExcluir);
                    if (produtoExcluir != null) {
                        produtos.excluir(produtoExcluir);
                        System.out.println("Produto excluído com sucesso!");
                    } else {
                        System.out.println("Produto não encontrado.");
                    }
                    break;

                case 0:
                    System.out.println("Voltando ao menu principal...");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        } while (operacao != 0);
    }


    public static void MontarItens(Produtos produtos, Itens itens, Scanner scanner){
        int operacao;
        do {
            System.out.println("\n--- Menu de Itens ---");
            System.out.println("1. Adicionar item");
            System.out.println("2. Listar itens");
            System.out.println("3. Atualizar item");
            System.out.println("4. Excluir item");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");
            operacao = scanner.nextInt();
            scanner.nextLine(); 



            switch (operacao) {
                case 1:
                    System.out.print("\nDigite o ID do Produto: ");
                    int idProduto = scanner.nextInt();
                    System.out.print("Digite o ID do Kit Solar: ");
                    int idKitSolar = scanner.nextInt();
                    System.out.print("Digite a quantidade: ");
                    int quantidade = scanner.nextInt();

                    itens.inserir(new Item(0, idProduto, idKitSolar, quantidade)); // ID 0 será gerado automaticamente
                    System.out.println("Item adicionado com sucesso!");
                    break;
                case 2:
                    // Listar itens
                    System.out.println("\nLista de Itens:");
                    for (Item item : itens.listar()) {
                        System.out.println(item);
                    }
                    break;
                
                case 3:
                    System.out.print("\nDigite o ID do item que deseja atualizar: ");
                    int idAtualizar = scanner.nextInt();
                    Item itemAtualizado = itens.listarId(idAtualizar);

                    if (itemAtualizado != null) {
                        System.out.print("Digite a nova quantidade: ");
                        int novaQuantidade = scanner.nextInt();
                        itemAtualizado.setquantidade(novaQuantidade);
                        itens.atualizar(itemAtualizado);
                        System.out.println("Item atualizado com sucesso!");
                    } else {
                        System.out.println("Item não encontrado.");
                    }
                    break;

                case 4:
                    System.out.print("\nDigite o ID do item que deseja excluir: ");
                    int idExcluir = scanner.nextInt();
                    Item itemParaExcluir = itens.listarId(idExcluir);

                    if (itemParaExcluir != null) {
                        itens.excluir(itemParaExcluir);
                        System.out.println("Item excluído com sucesso!");
                    } else {
                        System.out.println("Item não encontrado.");
                    }
                    break;
                
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        } while (operacao != 0);
    }

    public static void KitsSolares(IdItem idItem, Quantidade quantidade, ValorKit valorKit, Scanner scanner){
        int operacao;
        do {
            System.out.println("\n--- Menu de Kits Solares ---");
            System.out.println("1. Adicionar kit");
            System.out.println("2. Listar kits");
            System.out.println("3. Atualizar kit");
            System.out.println("4. Excluir kit");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");
            operacao = scanner.nextInt();
            scanner.nextLine(); 



            switch (operacao) {
                case 1:
                    System.out.print("\nDigite o ID do Item: ");
                    int idProduto = scanner.nextInt();
                    System.out.print("Digite a quantidade: ");
                    int idKitSolar = scanner.nextInt();
                    System.out.print("Digite o valor do Kit: ");
                    int Quantidade = scanner.nextInt();

                    itens.inserir(new Item(0, idItem, quantidade, valorKit)); // ID 0 será gerado automaticamente
                    System.out.println("Kit adicionado com sucesso!");
                    break;
                case 2:
                    // Listar itens
                    System.out.println("\nLista de Kits Solares:");
                    for (Item item : itens.listar()) {
                        System.out.println(item);
                    }
                    break;
                
                case 3:
                    System.out.print("\nDigite o ID do kit que deseja atualizar: ");
                    int idAtualizar = scanner.nextInt();
                    Item itemAtualizado = itens.listarId(idAtualizar);

                    if (itemAtualizado != null) {
                        System.out.print("Digite a nova quantidade: ");
                        int novaQuantidade = scanner.nextInt();
                        itemAtualizado.setquantidade(novaQuantidade);
                        itens.atualizar(itemAtualizado);
                        System.out.println("Kit atualizado com sucesso!");
                    } else {
                        System.out.println("Kit não encontrado.");
                    }
                    break;

                case 4:
                    System.out.print("\nDigite o ID do kit que deseja excluir: ");
                    int idExcluir = scanner.nextInt();
                    Item itemParaExcluir = itens.listarId(idExcluir);

                    if (itemParaExcluir != null) {
                        itens.excluir(itemParaExcluir);
                        System.out.println("Kit excluído com sucesso!");
                    } else {
                        System.out.println("Kit não encontrado.");
                    }
                    break;
                
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        } while (operacao != 0);
    }
}