using System;

public class Empleado
{
    // Atributos privados
    private string nombre;
    private int anioContratacion;
    private double salario;

    // Propiedades publicas
    public string Nombre
    {
        get { return this.nombre; }
        set { this.nombre = value; }
    }

    public int AnioContratacion
    {
        get { return this.anioContratacion; }
        set { this.anioContratacion = value; }
    }

    public double Salario
    {
        get { return this.salario; }
        set { this.salario = value; }
    }

    // Constructores
    // Constructor vacio
    public Empleado()
    {
        this.nombre = "";
        this.anioContratacion = 0;
        this.salario = 0.0;
    }

    // Constructor con parametros
    public Empleado(string n, int a, double s)
    {
        this.nombre = n;
        this.anioContratacion = a;
        this.salario = s;
    }

    // Metodos
    public double calcularSalario()
    {
        return this.salario;
    }

    public override string ToString()
    {
        return 
            "\nNombre: " + this.nombre + 
            "\nAnio de Contratacion: " + this.anioContratacion + 
            "\nSalario: " + this.salario;
    }
}
