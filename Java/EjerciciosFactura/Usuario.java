package Java.EjerciciosFactura;

public class Usuario
{
    //Atributos
    String nombre;
    String apellido;
    int edad;
    
    public Usuario(){
        this.nombre = "";
        this.apellido ="";
        this.edad = 0;
    }
    
    //Sobrecarga de constructores
    public Usuario (String n, String a, int e){
        this.nombre = n;
        this.apellido = a;
        this.edad = e;
    }

    //Metodos
    void iniciarSesion()
    {
        System.out.println("El usuario " + this.nombre + " esta iniciando sesion.");
    }

    void hacerReporte()
    {
        System.out.println("Reporte de usuario");
        System.out.println("Nombre completo: " + this.nombre + " " + this.apellido);
        System.out.println("Edad: " + this.edad);
    }

    void cerrarSesion()
    {
        System.out.println("El usuario " + this.nombre + " esta cerrando sesion.");
    }
}