public class Empleado {
    // Atributos privados
    private String nombre;
    private int anioContratacion;
    private double salario;

    // Constructores
    // Constructor vacio
    public Empleado() {
        this.nombre = "";
        this.anioContratacion = 0;
        this.salario = 0.0;
    }

    // Constructor con parametros
    public Empleado(String n, int a, double s) {
        this.nombre = n;
        this.anioContratacion = a;
        this.salario = s;
    }

    // Getters y Setters (en lugar de propiedades C#)
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getAnioContratacion() {
        return this.anioContratacion;
    }

    public void setAnioContratacion(int anioContratacion) {
        this.anioContratacion = anioContratacion;
    }

    public double getSalario() {
        return this.salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    // Metodos
    public double calcularSalario() {
        return this.salario;
    }

    @Override
    public String toString() {
        return "\nNombre: " + this.nombre + 
               "\nAnio de Contratacion: " + this.anioContratacion + 
               "\nSalario: " + this.salario;
    }
}
