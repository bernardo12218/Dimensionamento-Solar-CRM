package admin.Models.src;

import java.util.HashMap;
import java.util.Map;

public class Local implements Inter{

    private int id;
    private int idItem;
    private int quantidade;
    private float valorKit;


    public Local(int id, int idItem, int quantidade, float valorKit){
        setId(id);
        setIdItem(idItem);
        setQuantidade(quantidade);
        setValorKit(valorKit);
    }

           // SETTERS
    public void setId(int id) {
        if (id >= 0) {
            this.id = id;
        }
         else {
            throw new IllegalArgumentException("ID não pode ser negativo");
        }
    }

    public void setIdItem(int idItem) {
        if (idItem >= 0) {
            this.idItem = idItem;
        }
         else {
            throw new IllegalArgumentException("Id do item não pode ser negativo");
        }
    }

    public void setQuantidade(int quantidade) {
        if (quantidade >= 0) {
            this.quantidade = quantidade;
        } 
        else {
            throw new IllegalArgumentException("Quantidade não pode ser negativa");
        }
    }

    public void setValorKit(float valorKit) {
        if (valorKit >= 0) {
            this.valorKit = valorKit;
        } 
        else {
            throw new IllegalArgumentException("ID do Kit Solar não pode ser negativo");
        }
    }


    // GETTERS
    public int getId() {
        return this.id;
    }

    public int getidItem() {
        return this.idItem;
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
        dict.put("idItem", this.idItem);
        dict.put("Quantidade", this.quantidade);
        dict.put("valorKit", this.valorKit);
        return dict;
    }

    @Override
    public String toString() {
        return "Kit Solar{" +
                "id=" + id +
                ", idItem=" + idItem +
                ", Quantidade=" + quantidade +
                ", ValorKit=" + valorKit +
                '}';
    }
}



