package Models.scr;


public class ClassItem {
    public class Item{
        private int id;
        private int id_Produto;
        private int id_KitSolar;
        private int quantidade;



        // CONSTRUTOR
        public Item(int id, int id_Produto, int id_KitSolar, int quantidade){
            set_Id(id);
            set_Id_Produto(id_Produto);
            set_Id_KitSolar(id_KitSolar);
            set_quantidade(quantidade);
        }
        // SETTERS

        public void set_Id(int id){
            if (id >= 0) {
                this.id = id;
            } else {
                throw new IllegalArgumentException("ID não pode ser negativo");
            }
        }

        public void set_Id_Produto(int id_Produto){
            if (id_Produto >= 0) {
                this.id_Produto = id_Produto;
            } else {
                throw new IllegalArgumentException("ID não pode ser negativo");
            }
        }

        public void set_Id_KitSolar(int id_KitSolar){
            if (id_KitSolar >= 0) {
                this.id_KitSolar = id_KitSolar;
            } else {
                throw new IllegalArgumentException("ID não pode ser negativo");
            }
        }

        public void set_quantidade(int quantidade){
            if (quantidade >= 0) {
                this.quantidade = quantidade;
            } else {
                throw new IllegalArgumentException("Quantidade não pode ser negativa");
            }
        }

        // GETTS
        public int get_Id(){
            return this.id;
        }

        public int get_Id_Produto(){
            return this.id_Produto;
        }

        public int get_Id_KitSolar(){
            return this.id_KitSolar;
        }

        public int get_Quantidade(){
            return this.quantidade;
        }

    }
}