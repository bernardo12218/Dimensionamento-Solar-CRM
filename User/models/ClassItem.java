import org.json.JSONArray;
import org.json.JSONObject;

import java.io.File;
import java.io.FileWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class ClassItem {

    // Class representing an Item
    public static class Item {
        private int id;
        private int idProduto;
        private int idKitSolar;
        private int quantidade;

        // Constructor
        public Item(int id, int idProduto, int idKitSolar, int quantidade) {
            this.setId(id);
            this.setIdProduto(idProduto);
            this.setIdKitSolar(idKitSolar);
            this.setQuantidade(quantidade);
        }

        // Setters with validation
        public void setId(int id) {
            if (id >= 0) {
                this.id = id;
            } else {
                throw new IllegalArgumentException("ID must be a non-negative integer.");
            }
        }

        public void setIdProduto(int idProduto) {
            if (idProduto >= 0) {
                this.idProduto = idProduto;
            } else {
                throw new IllegalArgumentException("ID Produto must be a non-negative integer.");
            }
        }

        public void setIdKitSolar(int idKitSolar) {
            if (idKitSolar >= 0) {
                this.idKitSolar = idKitSolar;
            } else {
                throw new IllegalArgumentException("ID Kit Solar must be a non-negative integer.");
            }
        }

        public void setQuantidade(int quantidade) {
            if (quantidade >= 0) {
                this.quantidade = quantidade;
            } else {
                throw new IllegalArgumentException("Quantidade must be a non-negative integer.");
            }
        }

        // Getters
        public int getId() {
            return id;
        }

        public int getIdProduto() {
            return idProduto;
        }

        public int getIdKitSolar() {
            return idKitSolar;
        }

        public int getQuantidade() {
            return quantidade;
        }

        // Convert to a JSON-like Map
        public JSONObject toDict() {
            JSONObject obj = new JSONObject();
            obj.put("id", id);
            obj.put("idProduto", idProduto);
            obj.put("idKitSolar", idKitSolar);
            obj.put("quantidade", quantidade);
            return obj;
        }

        // Create an Item from a JSON-like Map
        public static Item fromDict(JSONObject data) {
            return new Item(
                    data.getInt("id"),
                    data.getInt("idProduto"),
                    data.getInt("idKitSolar"),
                    data.getInt("quantidade")
            );
        }

        @Override
        public String toString() {
            return "Item { " +
                    "ID=" + id +
                    ", ID Produto=" + idProduto +
                    ", ID Kit Solar=" + idKitSolar +
                    ", Quantidade=" + quantidade +
                    " }";
        }
    }

    // Class managing a list of Items and saving/loading to/from JSON
    public static class Itens {
        private static final String ARQUIVO_JSON = "itens.json";
        private static List<Item> listaItens = new ArrayList<>();

        // Insert an item
        public static void inserir(Item item) {
            listaItens.add(item);
        }

        // List all items
        public static List<Item> listar() {
            return listaItens;
        }

        // Find an item by ID
        public static Item listarPorId(int id) {
            for (Item item : listaItens) {
                if (item.getId() == id) {
                    return item;
                }
            }
            return null;
        }

        // Update an item
        public static void atualizar(Item itemAtualizado) {
            for (int i = 0; i < listaItens.size(); i++) {
                if (listaItens.get(i).getId() == itemAtualizado.getId()) {
                    listaItens.set(i, itemAtualizado);
                    break;
                }
            }
        }

        // Delete an item
        public static void excluir(int id) {
            listaItens.removeIf(item -> item.getId() == id);
        }

        // Load items from JSON file
        public static void abrir() {
            listaItens.clear();
            File file = new File(ARQUIVO_JSON);
            if (!file.exists()) {
                System.out.println("JSON file not found. Creating a new one.");
                return;
            }

            try {
                String content = new String(Files.readAllBytes(Paths.get(ARQUIVO_JSON)));
                JSONArray jsonArray = new JSONArray(content);
                for (int i = 0; i < jsonArray.length(); i++) {
                    JSONObject obj = jsonArray.getJSONObject(i);
                    Item item = Item.fromDict(obj);
                    listaItens.add(item);
                }
                System.out.println("Items loaded successfully!");
            } catch (Exception e) {
                System.err.println("Error loading items: " + e.getMessage());
            }
        }

        // Save items to JSON file
        public static void salvar() {
            JSONArray jsonArray = new JSONArray();
            for (Item item : listaItens) {
                jsonArray.put(item.toDict());
            }

            try (FileWriter file = new FileWriter(ARQUIVO_JSON)) {
                file.write(jsonArray.toString(4));
                System.out.println("Items saved successfully!");
            } catch (Exception e) {
                System.err.println("Error saving items: " + e.getMessage());
            }
        }
    }

    // Main method for testing
    public static void main(String[] args) {
        // Load items from JSON (if any)
        Itens.abrir();

        // Create a new item
        Item item1 = new Item(0, 1, 2, 30);
        Itens.inserir(item1);

        // Save items to JSON
        Itens.salvar();

        // List all items
        System.out.println("Items saved:");
        for (Item item : Itens.listar()) {
            System.out.println(item);
        }
    }
}