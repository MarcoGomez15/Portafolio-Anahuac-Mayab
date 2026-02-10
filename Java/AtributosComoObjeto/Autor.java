//Atributos como objeto y método toString

package Java.AtributosComoObjeto;

public class Autor {
    String nombre;
    String nacionalidad;

    public Autor(String nombre, String nacionalidad) {
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
    }

    @Override
    public String toString(){
        return "Nombre: " + this.nombre + "\n" + "Nacionalidad: " + this.nacionalidad;
    }
}
