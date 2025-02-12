package admin.Models.src;

import java.util.HashMap;
import java.util.Map;

public class Produto implements Inter{

    private int id;
    private String tipo;
    private float valor;
    private int estoque;
    private String marca;
    private int potencia;

    public Produto(int id, String tipo, float valor, int estoque, String marca, int potencia){
        setId(id);
        setTipo(tipo);
        setValor(valor);
        setEstoque(estoque);
        setMarca(marca);
        setPotencia(potencia);
    }

    public void setId(int id) {
        if (id >= 0) {
            this.id = id;
        } else {
            throw new IllegalArgumentException("ID não pode ser negativo");
        }
    }

    public void setId(int id) {
        if (id >= 0) {
            this.id = id;
        } else {
            throw new IllegalArgumentException("ID não pode ser negativo");
        }
    }
}