public class Test {
    public static void main(String[] args) {
        // Se crea un objeto Triangulo
        Triangulo triangulo = new Triangulo(3, 5.0, 4.0);
        
        // Se crea un objeto Circunferencia
        Circunferencia circunferencia = new Circunferencia(0, 3.0);

        System.out.println("--- TRIANGULO ---");
        System.out.println("Numero de lados: " + triangulo.getNumLados());
        System.out.println("Area: " + triangulo.calcularArea());
        System.out.println("Perimetro: " + triangulo.calcularPerimetro());

        System.out.println("\n--- CIRCUNFERENCIA ---");
        System.out.println("Numero de lados: " + circunferencia.getNumLados());
        System.out.println("Area: " + circunferencia.calcularArea());
        System.out.println("Perimetro: " + circunferencia.calcularPerimetro());
    }
}
