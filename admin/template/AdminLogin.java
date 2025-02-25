package template;

import java.util.Scanner;


public class AdminLogin {
    public static void main(String[] args) {
        login();
    }

    public static boolean login() {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.print("Digite o email: ");
            String email = scanner.nextLine();
            System.out.print("Digite a senha: ");
            String senha = scanner.nextLine();

            if (email.equals("admin@gmail.com") && senha.equals("1234")) {
                return true;
            } else {
                System.out.println("Login Inválido!");
            }
        }
    }
}
