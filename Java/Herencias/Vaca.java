package Java.Herencias;

public class Vaca extends Mamifero {
    private double litrosLeche;

    public Vaca(String n, double p, double l){
        super(n, p); // Invoca al constructor de la clase padre
        this.litrosLeche = l;
    }

    public void calcularCantidadComida(){
        System.out.println(super.peso*0.03 + "kg de alimento");
    }

    @Override
    public String toString(){
        return super.toString() + "[litros de leche: " + litrosLeche + "]";
    }
}
