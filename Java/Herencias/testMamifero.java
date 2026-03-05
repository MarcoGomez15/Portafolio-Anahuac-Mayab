package Java.Herencias;

public class testMamifero {
    public static void main(String[] args) {
        Gato Michi = new Gato("Michi", 5, 12);
        Vaca Lola    = new Vaca("Lola", 500, 20);
        Ballena Willy = new Ballena("Willy", 5000);    

        System.out.println(Michi);
        System.out.println("");
        System.out.println(Lola);
        System.out.println("");
        System.out.println(Willy);

        Lola.calcularCantidadComida();
    }
}
