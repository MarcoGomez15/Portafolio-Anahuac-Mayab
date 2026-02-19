using System;


public class Autor {
    public string nombre;
    public string nacionalidad;

    public Autor(string nombre, string nacionalidad) {
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
    }

    public override string ToString(){
        return "Nombre: " + this.nombre + "\n" + "Nacionalidad: " + this.nacionalidad;
    }
}
