public class Circunferencia extends Poligono {
    protected double radio;

    public Circunferencia(int n, double radio) {
        this.numLados = n;
        this.radio = radio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * Math.pow(radio, 2);
    }

    @Override
    public double calcularPerimetro() {
        return 2 * Math.PI * radio;
    }
}
