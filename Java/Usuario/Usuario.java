package Java.Usuario;

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
    String iniciarSesion()
    {
        return "El usuario " + this.nombre + " esta iniciando sesion.";
    }

    String hacerReporte()
    {
        return ("Reporte de usuario") + ("\nNombre completo: " + this.nombre + " " + this.apellido + "\nEdad: " + this.edad);
    }

    String cerrarSesion()
    {
        return "El usuario " + this.nombre + " esta cerrando sesion.";
    }
}