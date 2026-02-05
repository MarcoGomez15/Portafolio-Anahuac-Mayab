import java.util.Scanner;

public class testEmpleado {
    public static void main(String[] args) {
        // Objeto 1 - constructor vacio
        System.out.println("--- Empleado 1 (Vacio) ---");
        Empleado emp1 = new Empleado();
        System.out.println(emp1.toString());

        // Objeto 2 - constructor con parametros
        System.out.println("--- Empleado 2 (Parametros) ---");
        Empleado emp2 = new Empleado("Donald Trump", 2025, 400000.99);
        System.out.println(emp2.toString());

        // Parte 2 - Solicitar datos al usuario
        System.out.println("\n--- Empleado 3 (Usuario) ---");
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresa el nombre del empleado:");
        String nom = scanner.nextLine();

        System.out.println("Ingrese el año de contratacion:");
        int anio = Integer.parseInt(scanner.nextLine());

        System.out.println("Ingrese el salario: ");
        double sal = Double.parseDouble(scanner.nextLine());

        Empleado emp3 = new Empleado(nom, anio, sal);
        System.out.println(emp3.toString());
        
        scanner.close();
    }
}