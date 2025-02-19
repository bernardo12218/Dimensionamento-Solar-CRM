// package admin.Models.src;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Locais extends CRUD<Local> {

    @Override
    public void salvar() {
        try (FileWriter writer = new FileWriter("./Data/Locais.json")) {
            Gson gson = new Gson();
            gson.toJson(objetos, writer);
            System.out.println("Itens salvos em 'Locais.json'.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void abrir() {
        objetos.clear();
        try (FileReader reader = new FileReader("./Data/Locais.json")) {
            Type listType = new TypeToken<List<Local>>() {}.getType();
            objetos = new Gson().fromJson(reader, listType);
            if (objetos == null) {
                objetos = new ArrayList<>(); // Inicializa a lista se o arquivo estiver vazio
            }
            System.out.println("Locais carregados de 'Locais.json'.");
        } catch (FileNotFoundException e) {
            objetos = new ArrayList<>(); // Se o arquivo não existir, cria uma lista vazia
            System.out.println("Arquivo 'Locais.json' não encontrado. Criando nova lista de locais.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}