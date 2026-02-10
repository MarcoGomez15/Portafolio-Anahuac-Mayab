using System;

class Usuario
{
    // Atributos
    private string nombre = "";
    private string apellidos = "";
    private int edad;
    

    // Constructor por defecto
    public Usuario()
    {
        this.nombre = "";
        this.apellidos = "";
        this.edad = 0;
    }

    // Constructor
    public Usuario(string nombre, string apellidos, int edad)
    {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.edad = edad;
    }

    // Setter y getter
    public String Nombre
    {
        get { return this.nombre; }
        set { this.nombre = value; }
    }

    public String Apellidos
    {
        get { return this.apellidos; }
        set { this.apellidos = value; }
    }

    public int Edad
    {
        get { return this.edad; }
        set { this.edad = value; }
    }

    // Métodos
    public void hacerReporte()
    {
        Console.WriteLine("El usuario " + this.nombre + " esta iniciando sesion.");
    }

    public void iniciarSesion() 
    {
        Console.WriteLine("El usuario " + this.nombre + " ha cerrado la sesion.");
    }

    public void cerrarSesion() 
    {
        Console.WriteLine("Reporte de usuario");
        Console.WriteLine("Nombre completo: " + this.nombre + " " + this.apellidos);
        Console.WriteLine("Edad: " + this.edad);
    }
}