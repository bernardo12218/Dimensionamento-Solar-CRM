// package admin.Models.src;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.List;
import java.util.List;
import java.util.ArrayList;

public class KitsSolares extends CRUD<KitSolar> {

    @Override
    public void salvar() {
        try (FileWriter writer = new FileWriter("./Data/KitsSolares.json")) {
            Gson gson = new Gson();
            gson.toJson(objetos, writer);
            System.out.println("Kits solares salvos em 'KitsSolares.json'.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void abrir() {
        objetos.clear();
        try (FileReader reader = new FileReader("./Data/KitsSolares.json")) {
            Type listType = new TypeToken<List<KitSolar>>() {}.getType();
            objetos = new Gson().fromJson(reader, listType);
            if (objetos == null) {
                objetos = new ArrayList<>();
            }
            System.out.println("Kits solares carregados de 'KitsSolares.json'.");
        } catch (FileNotFoundException e) {
            objetos = new ArrayList<>();
            System.out.println("Arquivo 'KitsSolares.json' não encontrado. Criando nova lista de kits solares.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}