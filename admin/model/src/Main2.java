// // package admin.Models.src;

// import java.util.Scanner;
// import java.util.ArrayList;
// import java.util.List;

// public class Main2 {
//     public static void Main2(String[] args) {
//         Produtos produtos = new Produtos(); 
//         Itens itens = new Itens();
//         Locais locais = new Locais();
//         KitsSolares kitsSolares = new KitsSolares();

//         Scanner scanner = new Scanner(System.in); 

//         int opcao;

//         do {
//             System.out.println("\n--- Menu Principal ---");
//             System.out.println("1. Gerenciar Produtos");
//             System.out.println("2. Gerenciar Itens");
//             System.out.println("3. Gerenciar Locais");
//             System.out.println("4. Montar Kits");
//             System.out.println("0. Sair");
//             System.out.print("Escolha uma opção: ");
//             opcao = scanner.nextInt();
//             scanner.nextLine(); 

//             switch (opcao) {
//                 case 1:
//                     gerenciarProdutos(produtos, scanner); 
//                     break;

//                 case 2:
//                     MontarItens(produtos, itens, kitsSolares, scanner);
//                     break;

//                 case 3:
//                     gerenciarLocais(locais, scanner);
//                     break;

//                 case 4:
//                     montarKitsSolares(kitsSolares, scanner);
//                     break;

//                 case 0:
//                     System.out.println("Saindo...");
//                     break;

//                 default:
//                     System.out.println("Opção inválida. Tente novamente.");
//                     break;
//             }
//         } while (opcao != 0);

//         scanner.close(); // Fechar o scanner ao final
//     }

//     public static void gerenciarProdutos(Produtos produtos, Scanner scanner) {
//         int operacao;

//         do {
//             System.out.println("\n--- Menu de Produtos ---");
//             System.out.println("1. Adicionar Produto");
//             System.out.println("2. Listar Produtos");
//             System.out.println("3. Atualizar Produto");
//             System.out.println("4. Excluir Produto");
//             System.out.println("0. Voltar");
//             System.out.print("Escolha uma opção: ");
//             operacao = scanner.nextInt();
//             scanner.nextLine(); // Consumir a nova linha

//             switch (operacao) {
//                 case 1:
//                     System.out.println("\n--- ** Inserindo Produto ** ---");
//                     System.out.print("Digite o tipo do Produto: ");
//                     String tipoProduto = scanner.nextLine();
//                     System.out.print("Digite o valor do Produto: R$");
//                     float valor = scanner.nextFloat();
//                     System.out.print("Digite o estoque do Produto: ");
//                     int estoque = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
//                     System.out.print("Digite a marca do Produto: ");
//                     String marca = scanner.nextLine();
//                     System.out.print("Digite a potência do Produto (em Watts): ");
//                     int potencia = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha

//                     produtos.inserir(new Produto(0, tipoProduto, valor, estoque, marca, potencia));
//                     System.out.println("Produto adicionado com sucesso!");
//                     break;

//                 case 2:
//                     System.out.println("\n--- ** Listando Produtos ** ---");
//                     for (Produto produto : produtos.listar()) {
//                         System.out.println(produto);
//                     }
//                     break;

//                 case 3:
//                     System.out.println("\n--- ** Atualizando Produto ** ---");
//                     System.out.print("Digite o ID do produto que deseja atualizar: ");
//                     int idAtualizar = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha

//                     Produto produtoAtualizado = produtos.listarId(idAtualizar);
//                     if (produtoAtualizado != null) {
//                         System.out.print("Digite o novo tipo do Produto: ");
//                         String novoTipo = scanner.nextLine();
//                         System.out.print("Digite o novo valor do Produto: R$");
//                         float novoValor = scanner.nextFloat();
//                         System.out.print("Digite o novo estoque do Produto: ");
//                         int novoEstoque = scanner.nextInt();
//                         scanner.nextLine(); // Consumir a nova linha
//                         System.out.print("Digite a nova marca do Produto: ");
//                         String novaMarca = scanner.nextLine();
//                         System.out.print("Digite a nova potência do Produto (em Watts): ");
//                         int novaPotencia = scanner.nextInt();
//                         scanner.nextLine(); // Consumir a nova linha

//                         produtoAtualizado.setTipo(novoTipo);
//                         produtoAtualizado.setValor(novoValor);
//                         produtoAtualizado.setEstoque(novoEstoque);
//                         produtoAtualizado.setMarca(novaMarca);
//                         produtoAtualizado.setPotencia(novaPotencia);

//                         produtos.atualizar(produtoAtualizado);
//                         System.out.println("Produto atualizado com sucesso!");
//                     } else {
//                         System.out.println("Produto não encontrado.");
//                     }
//                     break;

//                 case 4:
//                     System.out.println("\n--- ** Excluindo Produto ** ---");
//                     System.out.print("Digite o ID do produto que deseja excluir: ");
//                     int idExcluir = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha

//                     Produto produtoExcluir = produtos.listarId(idExcluir);
//                     if (produtoExcluir != null) {
//                         produtos.excluir(produtoExcluir);
//                         System.out.println("Produto excluído com sucesso!");
//                     } else {
//                         System.out.println("Produto não encontrado.");
//                     }
//                     break;

//                 case 0:
//                     System.out.println("Voltando ao menu principal...");
//                     break;

//                 default:
//                     System.out.println("Opção inválida. Tente novamente.");
//                     break;
//             }
//         } while (operacao != 0);
//     }

//     public static void MontarItens(Produtos produtos, Itens itens, KitsSolares kitsSolares, Scanner scanner) {
//         int operacao;
//         do {
//             System.out.println("\n--- Menu de Itens ---");
//             System.out.println("1. Adicionar item");
//             System.out.println("2. Listar itens");
//             System.out.println("3. Atualizar item");
//             System.out.println("4. Excluir item");
//             System.out.println("0. Sair");
//             System.out.print("Escolha uma opção: ");
//             operacao = scanner.nextInt();
//             scanner.nextLine(); // Consumir a nova linha
    
//             switch (operacao) {
//                 case 1:
//                     System.out.println("\n--- Adicionar Item ---");
    
//                     // Listar produtos disponíveis
//                     System.out.println("Lista de Produtos:");
//                     for (Produto produto : produtos.listar()) {
//                         System.out.println(produto);
//                     }
    
//                     // Solicitar o ID do produto
//                     System.out.print("Digite o ID do Produto: ");
//                     int idProduto = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
    
//                     // Verificar se o produto existe
//                     Produto produtoSelecionado = produtos.listarId(idProduto);
//                     if (produtoSelecionado == null) {
//                         System.out.println("Produto não encontrado.");
//                         break;
//                     }
    
//                     // Listar kits solares disponíveis
//                     System.out.println("Lista de Kits Solares:");
//                     for (KitSolar kit : kitsSolares.listar()) {
//                         System.out.println(kit);
//                     }
    
//                     // Solicitar o ID do kit solar
//                     System.out.print("Digite o ID do Kit Solar (ou 0 para criar um novo): ");
//                     int idKitSolar = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
    
//                     KitSolar kitSelecionado = null;
    
//                     if (idKitSolar == 0) {
//                         // Criar um novo kit solar com uma lista vazia de IDs dos itens
//                         System.out.print("Digite a quantidade do kit solar: ");
//                         int quantidadeKit = scanner.nextInt();
//                         System.out.print("Digite o valor total do kit solar: R$");
//                         float valorKit = scanner.nextFloat();
//                         scanner.nextLine(); // Consumir a nova linha
    
//                         kitSelecionado = new KitSolar(0, new ArrayList<>(), quantidadeKit, valorKit);
//                         kitsSolares.inserir(kitSelecionado);
//                         System.out.println("Novo kit solar criado com sucesso!");
//                         idKitSolar = kitSelecionado.getId(); // Obter o ID do kit solar criado
//                     } else {
//                         // Verificar se o kit solar existe
//                         kitSelecionado = kitsSolares.listarId(idKitSolar);
//                         if (kitSelecionado == null) {
//                             System.out.println("Kit Solar não encontrado.");
//                             break;
//                         }
//                     }
    
//                     // Solicitar a quantidade do item
//                     System.out.print("Digite a quantidade: ");
//                     int quantidade = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
    
//                     // Criar o item
//                     itens.inserir(new Item(0, idProduto, idKitSolar, quantidade));
//                     System.out.println("Item adicionado com sucesso!");
//                     break;
    
//                 case 2:
//                     System.out.println("\n--- Listar Itens ---");
//                     for (Item item : itens.listar()) {
//                         System.out.println(item);
//                     }
//                     break;
    
//                 case 3:
//                     System.out.println("\n--- Atualizar Item ---");
//                     System.out.print("Digite o ID do item que deseja atualizar: ");
//                     int idAtualizar = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
    
//                     Item itemAtualizado = itens.listarId(idAtualizar);
//                     if (itemAtualizado != null) {
//                         System.out.print("Digite a nova quantidade: ");
//                         int novaQuantidade = scanner.nextInt();
//                         scanner.nextLine(); // Consumir a nova linha
    
//                         itemAtualizado.setquantidade(novaQuantidade);
//                         itens.atualizar(itemAtualizado);
//                         System.out.println("Item atualizado com sucesso!");
//                     } else {
//                         System.out.println("Item não encontrado.");
//                     }
//                     break;
    
//                 case 4:
//                     System.out.println("\n--- Excluir Item ---");
//                     System.out.print("Digite o ID do item que deseja excluir: ");
//                     int idExcluir = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
    
//                     Item itemExcluir = itens.listarId(idExcluir);
//                     if (itemExcluir != null) {
//                         itens.excluir(itemExcluir);
//                         System.out.println("Item excluído com sucesso!");
//                     } else {
//                         System.out.println("Item não encontrado.");
//                     }
//                     break;
    
//                 case 0:
//                     System.out.println("Voltando ao menu principal...");
//                     break;
    
//                 default:
//                     System.out.println("Opção inválida. Tente novamente.");
//                     break;
//             }
//         } while (operacao != 0);
//     }
    
//     public static void montarKitsSolares(KitsSolares kitsSolares, Scanner scanner) {
//         int operacao;
    
//         do {
//             System.out.println("\n--- Menu Kits Solares ---");
//             System.out.println("1. Criar Kit Solar");
//             System.out.println("2. Listar Kits Solares");
//             System.out.println("3. Atualizar Kit Solar");
//             System.out.println("4. Excluir Kit Solar");
//             System.out.println("0. Sair");
//             System.out.print("Escolha uma opção: ");
//             operacao = scanner.nextInt();
//             scanner.nextLine(); // Consumir a nova linha
    
//             switch (operacao) {
//                 case 1:
//                     System.out.println("\n--- Criar Kit Solar ---");
    
//                     // Solicitar a quantidade e o valor do kit solar
//                     System.out.print("Digite a quantidade do kit solar: ");
//                     int quantidade = scanner.nextInt();
//                     System.out.print("Digite o valor total do kit solar: R$");
//                     float valorKit = scanner.nextFloat();
//                     scanner.nextLine(); // Consumir a nova linha
    
//                     // Criar o kit solar sem itens inicialmente
//                     kitsSolares.inserir(new KitSolar(0, new ArrayList<>(), quantidade, valorKit));
//                     System.out.println("Kit solar criado com sucesso!");
//                     break;
    
//                 case 2:
//                     System.out.println("\n--- Listar Kits Solares ---");
//                     for (KitSolar kit : kitsSolares.listar()) {
//                         System.out.println(kit);
//                     }
//                     break;
    
//                 case 3:
//                     System.out.println("\n--- Atualizar Kit Solar ---");
//                     System.out.print("Digite o ID do kit solar que deseja atualizar: ");
//                     int idAtualizar = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
    
//                     KitSolar kitAtualizado = kitsSolares.listarId(idAtualizar);
//                     if (kitAtualizado != null) {
//                         System.out.print("Digite a nova quantidade: ");
//                         int novaQuantidade = scanner.nextInt();
//                         System.out.print("Digite o novo valor total: R$");
//                         float novoValor = scanner.nextFloat();
//                         scanner.nextLine(); // Consumir a nova linha
    
//                         kitAtualizado.setQuantidade(novaQuantidade);
//                         kitAtualizado.setValorKit(novoValor);
//                         kitsSolares.atualizar(kitAtualizado);
//                         System.out.println("Kit solar atualizado com sucesso!");
//                     } else {
//                         System.out.println("Kit solar não encontrado.");
//                     }
//                     break;
    
//                 case 4:
//                     System.out.println("\n--- Excluir Kit Solar ---");
//                     System.out.print("Digite o ID do kit solar que deseja excluir: ");
//                     int idExcluir = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
    
//                     KitSolar kitExcluir = kitsSolares.listarId(idExcluir);
//                     if (kitExcluir != null) {
//                         kitsSolares.excluir(kitExcluir);
//                         System.out.println("Kit solar excluído com sucesso!");
//                     } else {
//                         System.out.println("Kit solar não encontrado.");
//                     }
//                     break;
    
//                 case 0:
//                     System.out.println("Voltando ao menu principal...");
//                     break;
    
//                 default:
//                     System.out.println("Opção inválida. Tente novamente.");
//                     break;
//             }
//         } while (operacao != 0);
//     }


//     public static void gerenciarLocais(Locais locais, Scanner scanner) {
//         int operacao;

//         do  {   
//             System.out.println("\n--- Menu de Locais ---");
//             System.out.println("1. Adicionar local");
//             System.out.println("2. Listar locais");
//             System.out.println("3. Atualizar local");
//             System.out.println("4. Excluir local");
//             System.out.println("0. Sair");
//             System.out.print("Escolha uma opção: ");
//             operacao = scanner.nextInt();
//             scanner.nextLine(); 

//             switch (operacao)   {
//                 case 1:
//                     System.out.print("\nDigite o nome da cidade: ");
//                     String cidade = scanner.nextLine();
//                     System.out.print("Digite a irradiação média da cidade: ");
//                     float irradiacao = scanner.nextFloat();
//                     locais.inserir(new Local(0, cidade, irradiacao));
//                     System.out.println("Local adicionado com sucesso!");
//                     break;

//                 case 2:
//                     System.out.println("\nLista de Locais:");
//                     for (Local local : locais.listar()) {
//                         System.out.println(local);
//                     }
//                     break;

//                 case 3:
//                     System.out.print("\nDigite o ID do local que deseja atualizar: ");
//                     int idAtualizar = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
//                     Local localAtualizado = locais.listarId(idAtualizar);

//                     if (localAtualizado != null) {
//                         System.out.print("Digite a nova cidade: ");
//                         String novaCidade = scanner.nextLine();
//                         System.out.print("Digite a irradiação da nova cidade: ");
//                         float novaIrradiacao = scanner.nextFloat();
//                         scanner.nextLine(); // Consumir a nova linha

//                         localAtualizado.setCidade(novaCidade);
//                         localAtualizado.setIrradiacao(novaIrradiacao);
//                         locais.atualizar(localAtualizado);
//                         System.out.println("Local atualizado com sucesso!");
//                     } else {
//                         System.out.println("Local não encontrado.");
//                     }
//                     break;

//                 case 4:
//                     System.out.print("\nDigite o ID do local que deseja excluir: ");
//                     int idExcluir = scanner.nextInt();
//                     scanner.nextLine(); // Consumir a nova linha
//                     Local localExcluir = locais.listarId(idExcluir);

//                     if (localExcluir != null) {
//                         locais.excluir(localExcluir);
//                         System.out.println("Local excluído com sucesso!");
//                     } else {
//                         System.out.println("Local não encontrado.");
//                     }
//                     break;

//                 case 0:
//                     System.out.println("Voltando ao menu principal...");
//                     break;

//                 default:
//                     System.out.println("Opção inválida. Tente novamente.");
//                     break;
//             }
//         } while (operacao != 0);
//     }


// }