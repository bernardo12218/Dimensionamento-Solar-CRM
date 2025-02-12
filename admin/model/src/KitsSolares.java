package admin.Models.src;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class KitsSolares extends CRUD<KitSolar> {

    @Override
    public void salvar() {
        try (FileWriter writer = new FileWriter("KitsSolares.json")) {
            Gson gson = new Gson();
            gson.toJson(objetos, writer);
            System.out.println("Itens salvos em 'KitsSolares.json'.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void abrir() {
        objetos.clear();
        try (FileReader reader = new FileReader("KitsSolares.json")) {
            Type listType = new TypeToken<List<Item>>() {}.getType();
            objetos = new Gson().fromJson(reader, listType);
            if (objetos == null) {
                objetos = new ArrayList<>(); // Inicializa a lista se o arquivo estiver vazio
            }
            System.out.println("Kits Solares carregados de 'KitsSolares.json'.");
        } catch (FileNotFoundException e) {
            objetos = new ArrayList<>(); // Se o arquivo não existir, cria uma lista vazia
            System.out.println("Arquivo 'KitsSolares.json' não encontrado. Criando nova lista de kitssolares.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}