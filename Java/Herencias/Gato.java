package Java.Herencias;

public class Gato extends Mamifero {
    private int nBigotes;

    public Gato(String n, double p, int b){
        super(n, p); // Invoca al constructor de la clase padre
        this.nBigotes = b;
    }

    @Override
    public String toString(){
        return super.toString() +"[Bigotes: " + nBigotes + "]";
    }
}
