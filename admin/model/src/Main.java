package admin.Models.src;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Itens itens = new Itens();
        Scanner scanner = new Scanner(System.in);
        int opcao;

        do {
            // Exibir menu
            System.out.println("\n--- Menu de Itens ---");
            System.out.println("1. Listar itens");
            System.out.println("2. Adicionar item");
            System.out.println("3. Atualizar item");
            System.out.println("4. Excluir item");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            
            scanner.nextLine(); // Consumir a nova linha

            switch (opcao) {
                case 1:
                    // Listar itens
                    System.out.println("\nLista de Itens:");
                    for (Item item : itens.listar()) {
                        System.out.println(item);
                    }
                    break;

                case 2:
                    // Adicionar item
                    System.out.print("\nDigite o ID do Produto: ");
                    int idProduto = scanner.nextInt();
                    System.out.print("Digite o ID do Kit Solar: ");
                    int idKitSolar = scanner.nextInt();
                    System.out.print("Digite a quantidade: ");
                    int quantidade = scanner.nextInt();

                    itens.inserir(new Item(0, idProduto, idKitSolar, quantidade)); // ID 0 será gerado automaticamente
                    System.out.println("Item adicionado com sucesso!");
                    break;

                case 3:
                    // Atualizar item
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
                    // Excluir item
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
                    // Sair
                    System.out.println("Saindo...");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        } while (opcao != 0);

        do {
            // Exibir menu
            System.out.println("\n--- Menu de Locais ---");
            System.out.println("1. Listar Locais");
            System.out.println("2. Adcionar Local");
            System.out.println("3. Atualizar Local");
            System.out.println("4. Excluir Local");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine(); // Consumir a nova linha

            switch (opcao) {
                case 1:
                    // Listar locais
                    System.out.println("\nLista de Locais:");
                    for (Item local : locais.listar()) {
                        System.out.println(local);
                    }
                    break;

                case 2:
                    // Adicionar Local
                    System.out.print("\nDigite o nome da cidade: ");
                    String cidade = scanner.nextInt();
                    System.out.print("Digite a irradiação do local: ");
                    float irradiacao = scanner.nextInt();
                   

                    locais.inserir(new Local(0, cidade, irradiacao)); // ID 0 será gerado automaticamente
                    System.out.println("Local adicionado com sucesso!");
                    break;

                case 3:
                    // Atualizar local
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
                    // Excluir item
                    System.out.print("\nDigite o ID do local que deseja excluir: ");
                    int idExcluir = scanner.nextInt();
                    Item itemParaExcluir = locais.listarId(idExcluir);

                    if (itemParaExcluir != null) {
                        itens.excluir(itemParaExcluir);
                        System.out.println("Local excluído com sucesso!");
                    } else {
                        System.out.println("Local não encontrado.");
                    }
                    break;

                case 0:
                    // Sair
                    System.out.println("Saindo...");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        } while (opcao != 0);

        scanner.close();
    }
}