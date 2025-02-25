package view

import admin.model.Produto;
import admin.model.Produtos;
import admin.model.Local;
import admin.model.Locais;
import admin.model.KitSolar;
import admin.model.KitsSolares;
import admin.model.Item;
import admin.model.Itens;

import java.util.List;

public class AdminView {
 
    // =========== Gerenciamento de Produtos ================
    public static void inserirProduto(String tipo, float valor, int estoque, String marca, int potencia) {
        Produto novoProduto = new Produto(0, tipo, valor, estoque, marca, potencia);
        Produtos.inserir(novoProduto);
    }

    public static List<Produto> listarProdutos() {
        return Produtos.listar();
    }

    public static void atualizarProduto(int id, String tipo, float valor, int estoque, String marca, int potencia) {
        Produto novoProduto = new Produto(id, tipo, valor, estoque, marca, potencia);
        Produtos.atualizar(novoProduto);
    }

    public static void removerProduto(int id) {
        Produtos.excluir(id);
    }
    // =========== Fim-Gerenciamento de Produtos ================

    // =========== Gerenciamento de Kits Solares ================
    public static void inserirKitSolar(List<Integer> idItens, int quantidade, float valorKit) {
        KitSolar novoKitSolar = new KitSolar(0, idItens, quantidade, valorKit);
        KitsSolar.inserir(novoKitSolar);
    }

    public static List<KitSolar> listarKitsSolar() {
        return KitsSolar.listar();
    }

    public static void atualizarKitSolar(int id, List<Integer> idItens, int quantidade, float valorKit) {
        KitSolar novoKitSolar = new KitSolar(id, idItens, quantidade, valorKit);
        KitsSolar.atualizar(novoKitSolar);
    }

    public static void removerKitSolar(int id) {
        KitsSolar.excluir(id);
    }
    // =========== Fim-Gerenciamento de Kits Solares ================

    // =========== Gerenciamento de Locais ================
    public static void inserirLocal(String cidade, float irradiacao) {
        Local novoLocal = new Local(0, cidade, irradiacao);
        Locais.inserir(novoLocal);
    }

    public static List<Local> listarLocais() {
        return Locais.listar();
    }

    public static void atualizarLocal(int id, String cidade, float irradiacao) {
        Local novoLocal = new Local(id, cidade, irradiacao);
        Locais.atualizar(novoLocal);
    }

    public static void removerLocal(int id) {
        Locais.excluir(id);
    }
    // =========== Fim-Gerenciamento de Locais ================

    // =========== Gerenciamento de Itens ================
    public static void inserirItem(int id_Produto, int id_KitSolar, int quantidade) {
        Item novoItem = new Item(0, id_Produto, id_KitSolar, quantidade);
        Itens.inserir(novoItem);
    }

    public static List<Integer> listarItens() {
        return Itens.listar();
    }

    public static void atualizarItem(int id, int id_Produto, int id_KitSolar, int quantidade) {
        Item novoItem = new Item(id, id_Produto, id_KitSolar, quantidade);
        Itens.atualizar(novoItem);
    }

    public static void removerItem(int id) {
        Itens.excluir(id);
    }
    // =========== Fim-Gerenciamento de Itens ================

    // =========== Montar Kits Solares ================
    public static void montarKitSolar(int quantidade, List<Integer> itens, float valorKit) {
        KitSolar novoKitSolar = KitsSolares.buscar(id);
        
    }
    // =========== Fim-Montar Kits Solares ================
}

