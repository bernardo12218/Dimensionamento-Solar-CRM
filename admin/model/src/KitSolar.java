// package admin.Models.src;

import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class KitSolar implements Inter {

    private int id;
    private List<Integer> idItens; // Lista de IDs dos itens
    private int quantidade;
    private float valorKit;

    // Construtor
    public KitSolar(int id, List<Integer> idItens, int quantidade, float valorKit) {
        setId(id);
        setIdItens(idItens); // Agora permite lista vazia
        setQuantidade(quantidade);
        setValorKit(valorKit);
    }

    // SETTERS
    public void setId(int id) {
        if (id >= 0) {
            this.id = id;
        } else {
            throw new IllegalArgumentException("ID não pode ser negativo");
        }
    }

    public void setIdItens(List<Integer> idItens) {
        if (idItens != null) { // Permite lista vazia, mas não nula
            this.idItens = idItens;
        } else {
            throw new IllegalArgumentException("A lista de IDs dos itens não pode ser nula");
        }
    }

    public void setQuantidade(int quantidade) {
        if (quantidade >= 0) {
            this.quantidade = quantidade;
        } else {
            throw new IllegalArgumentException("Quantidade não pode ser negativa");
        }
    }

    public void setValorKit(float valorKit) {
        if (valorKit >= 0) {
            this.valorKit = valorKit;
        } else {
            throw new IllegalArgumentException("Valor do kit não pode ser negativo");
        }
    }

    // GETTERS
    public int getId() {
        return this.id;
    }

    public List<Integer> getIdItens() {
        return this.idItens;
    }

    public int getQuantidade() {
        return this.quantidade;
    }

    public float getValorKit() {
        return this.valorKit;
    }

    // Método para converter o objeto em um Map (dicionário)
    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("idItens", this.idItens); // Agora é uma lista de IDs
        dict.put("quantidade", this.quantidade);
        dict.put("valorKit", this.valorKit);
        return dict;
    }

    // Método para exibir o objeto como uma string
    @Override
    public String toString() {
        return "Kit Solar{" +
                "id=" + id +
                ", idItens=" + idItens +
                ", quantidade=" + quantidade +
                ", valorKit=" + valorKit +
                '}';
    }
}