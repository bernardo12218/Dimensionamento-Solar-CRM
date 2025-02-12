package admin.Models.src;

import java.util.HashMap;
import java.util.Map;

public class Item implements Inter {
    private int id;
    private int id_Produto;
    private int id_KitSolar;
    private int quantidade;

    // Construtor
    public Item(int id, int id_Produto, int id_KitSolar, int quantidade) {
        setId(id);
        setId_Produto(id_Produto);
        setId_KitSolar(id_KitSolar);
        setquantidade(quantidade);
    }

    // SETTERS
    public void setId(int id) {
        if (id >= 0) {
            this.id = id;
        } else {
            throw new IllegalArgumentException("ID não pode ser negativo");
        }
    }

    public void setId_Produto(int id_Produto) {
        if (id_Produto >= 0) {
            this.id_Produto = id_Produto;
        } else {
            throw new IllegalArgumentException("ID não pode ser negativo");
        }
    }

    public void setId_KitSolar(int id_KitSolar) {
        if (id_KitSolar >= 0) {
            this.id_KitSolar = id_KitSolar;
        } else {
            throw new IllegalArgumentException("ID não pode ser negativo");
        }
    }

    public void setquantidade(int quantidade) {
        if (quantidade >= 0) {
            this.quantidade = quantidade;
        } else {
            throw new IllegalArgumentException("Quantidade não pode ser negativa");
        }
    }

    // GETTERS
    public int getId() {
        return this.id;
    }

    public int getId_Produto() {
        return this.id_Produto;
    }

    public int getId_KitSolar() {
        return this.id_KitSolar;
    }

    public int getQuantidade() {
        return this.quantidade;
    }

    // Método para converter o objeto em um Map (dicionário)
    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("id_Produto", this.id_Produto);
        dict.put("id_KitSolar", this.id_KitSolar);
        dict.put("quantidade", this.quantidade);
        return dict;
    }

    // Método para exibir o objeto como uma string
    @Override
    public String toString() {
        return "Item{" +
                "id=" + id +
                ", id_Produto=" + id_Produto +
                ", id_KitSolar=" + id_KitSolar +
                ", quantidade=" + quantidade +
                '}';
    }
}