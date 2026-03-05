package Java.Herencias;

public class Ballena extends Mamifero {
    public Ballena(String n, double p){
        super(n, p);
    }

    @Override
    public String toString(){
        return super.toString() + "[Ballena]";
    }
}
