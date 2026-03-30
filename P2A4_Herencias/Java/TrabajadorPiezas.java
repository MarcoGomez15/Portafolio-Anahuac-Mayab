public class TrabajadorPiezas extends Empleado {
    private double salario; // salario por pieza
    private int piezas; // número de piezas producidas

    public TrabajadorPiezas(String nombre, String apellido, String nss, double salario, int piezas) {
        super(nombre, apellido, nss);
        establecerSalario(salario);
        establecerPiezas(piezas);
    }

    public void establecerSalario(double salario) {
        this.salario = (salario >= 0.0) ? salario : 0.0;
    }

    public double obtenerSalario() {
        return salario;
    }

    public void establecerPiezas(int piezas) {
        this.piezas = (piezas >= 0) ? piezas : 0;
    }

    public int obtenerPiezas() {
        return piezas;
    }

    @Override
    public double ingresos() {
        return obtenerSalario() * obtenerPiezas();
    }

    @Override
    public String toString() {
        return String.format("trabajador por piezas: %s\n%s: $%,.2f; %s: %d",
                super.toString(), "salario por pieza", obtenerSalario(), "piezas producidas", obtenerPiezas());
    }
}
