// package admin.Models.src;

import java.util.HashMap;
import java.util.Map;

public class Local implements Inter{

    private int id;
    private String cidade;
    private float irradiacao;


    public Local(int id, String cidade, float irradiacao){
        setId(id);
        setCidade(cidade);
        setIrradiacao(irradiacao);
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

    public void setCidade(String cidade) {
            this.cidade = cidade;
      
    }

    public void setIrradiacao(float irradiacao) {
        if (irradiacao >= 0) {
            this.irradiacao = irradiacao;
        } 
        else {
            throw new IllegalArgumentException("Irradiacao não pode ser negativa");
        }
    }

    // GETTERS
    public int getId() {
        return this.id;
    }

    public String getCidade() {
        return this.cidade;
    }

    public float getIrradiacao() {
        return this.irradiacao;
    }

    // Método para converter o objeto em um Map (dicionário)
    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("Cidade", this.cidade);
        dict.put("Irradiação", this.irradiacao);
        return dict;
    }

    @Override
    public String toString() {
        return "Local{" +
                "id=" + id +
                ", Cidade=" + cidade +
                ", irradiação=" + irradiacao +
                '}';
    }
}



