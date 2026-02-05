package Java.EjerciciosFactura;

public class Usuario
{
    //Atributos
    private String nombre;
    private String apellidos;
    private int edad;
    
    public Usuario(){
        this.nombre = "";
        this.apellidos ="";
        this.edad = 0;
    }
    
    //Sobrecarga de constructores
    public Usuario (String n, String a, int e){
        this.nombre = n;
        this.apellidos = a;
        this.edad = e;
    }

    // Definir los setter y getter
public void setNombre(String n) {
   this.nombre = n; 
  }
String getNombre() {
   return this.nombre; 
  }
public void setApellidos(String a) {
   this.apellidos = a; 
  }
String getApellidos() {
   return this.apellidos; 
  }
public void setEdad(int e) {
   this.edad = e; 
  }
int getEdad() {
   return this.edad; 
  }

    //Metodos
    void iniciarSesion()
    {
        System.out.println("El usuario " + this.nombre + " esta iniciando sesion.");
    }

    void hacerReporte()
    {
        System.out.println("Reporte de usuario");
        System.out.println("Nombre completo: " + this.nombre + " " + this.apellidos);
        System.out.println("Edad: " + this.edad);
    }

    void cerrarSesion()
    {
        System.out.println("El usuario " + this.nombre + " esta cerrando sesion.");
    }
}