package P1A11_Termometro.Java;

import java.util.Scanner;

public class testTermometro {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. Instancia con constructor por defecto (aleatorio)
        System.out.println("--- Termometro 1 (Aleatorio) ---");
        Termometro t1 = new Termometro();
        t1.mostrarTemperaturas();
        System.out.println("------------------------------");

        // 2. Instancia con constructor parametrizado (usuario)
        System.out.println("--- Termometro 2 (Usuario) ---");
        System.out.print("Ingrese la temperatura en Celsius: ");
        
        if (sc.hasNextDouble()) {
            double tempUsuario = sc.nextDouble(); // Leer temperatura del usuario
            Termometro t2 = new Termometro(tempUsuario); // Usar constructor parametrizado
            t2.mostrarTemperaturas();
        } else {
            System.out.println("Error: Por favor ingrese un numero valido.");
        }
        System.out.println("------------------------------");
        
        sc.close();
    }
}