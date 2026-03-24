public class Triangulo extends Poligono {
    protected double base;
    protected double altura;

    public Triangulo(int n, double base, double altura) {
        this.numLados = n;
        this.base = base;
        this.altura = altura;
    }

    @Override
    public double calcularArea() {
        return (base * altura) / 2.0;
    }

    @Override
    public double calcularPerimetro() {
        return base * 3.0;
    }
}
