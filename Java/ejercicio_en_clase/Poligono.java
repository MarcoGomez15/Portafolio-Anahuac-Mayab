public abstract class Poligono {
    protected int numLados;

    public void setNumLados(int n) {
        this.numLados = n;
    }

    public int getNumLados() {
        return numLados;
    }

    public abstract double calcularArea();
    public abstract double calcularPerimetro();
}
