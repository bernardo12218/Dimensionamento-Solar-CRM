package admin.Models.src;

import java.util.HashMap;
import java.util.Map;

public class Produto implements Inter {

    private int id;
    private String tipo;
    private float valor;
    private int estoque;
    private String marca;
    private int potencia;

    // Construtor
    public Produto(int id, String tipo, float valor, int estoque, String marca, int potencia) {
        setId(id);
        setTipo(tipo);
        setValor(valor);
        setEstoque(estoque);
        setMarca(marca);
        setPotencia(potencia);
    }

    // SETTERS
    public void setId(int id) {
        if (id >= 0) {
            this.id = id;
        } else {
            throw new IllegalArgumentException("ID não pode ser negativo");
        }
    }

    public void setTipo(String tipo) {
        if (tipo != null && !tipo.isEmpty()) {
            this.tipo = tipo;
        } else {
            throw new IllegalArgumentException("Tipo não pode ser nulo ou vazio");
        }
    }

    public void setValor(float valor) {
        if (valor >= 0) {
            this.valor = valor;
        } else {
            throw new IllegalArgumentException("Valor não pode ser negativo");
        }
    }

    public void setEstoque(int estoque) {
        if (estoque >= 0) {
            this.estoque = estoque;
        } else {
            throw new IllegalArgumentException("Estoque não pode ser negativo");
        }
    }

    public void setMarca(String marca) {
        if (marca != null && !marca.isEmpty()) {
            this.marca = marca;
        } else {
            throw new IllegalArgumentException("Marca não pode ser nula ou vazia");
        }
    }

    public void setPotencia(int potencia) {
        if (potencia >= 0) {
            this.potencia = potencia;
        } else {
            throw new IllegalArgumentException("Potência não pode ser negativa");
        }
    }

    // GETTERS
    public int getId() {
        return id;
    }

    public String getTipo() {
        return tipo;
    }

    public float getValor() {
        return valor;
    }

    public int getEstoque() {
        return estoque;
    }

    public String getMarca() {
        return marca;
    }

    public int getPotencia() {
        return potencia;
    }

    // Método para converter o objeto em um Map (dicionário)
    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("tipo", this.tipo);
        dict.put("valor", this.valor);
        dict.put("estoque", this.estoque);
        dict.put("marca", this.marca);
        dict.put("potencia", this.potencia);
        return dict;
    }

    // Método para exibir o objeto como uma string
    @Override
    public String toString() {
        return "Produto{" +
                "id=" + id +
                ", tipo='" + tipo + '\'' +
                ", valor=" + valor +
                ", estoque=" + estoque +
                ", marca='" + marca + '\'' +
                ", potencia=" + potencia +
                '}';
    }
}