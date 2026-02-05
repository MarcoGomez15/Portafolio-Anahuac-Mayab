package Java;

public class Test {

    public static void main(String[] args) {
        //nombreClase nombreObjeto = new nombreClase();
        Usuario maestra = new Usuario();
        Usuario alumno = new Usuario("Tom","Cruise",64);
        
        //Asignar valores a los atributos
        //maestra.nombre = "";
        //maestra.apellido = "";
        //maestra.edad = 0;
        
        

        //Llamada (invocacion) de metodos
        maestra.iniciarSesion();
        maestra.hacerReporte();
        maestra.cerrarSesion();
        
        System.out.println("");
        
        alumno.iniciarSesion();
        alumno.hacerReporte();
        alumno.cerrarSesion();
        
    }
}
