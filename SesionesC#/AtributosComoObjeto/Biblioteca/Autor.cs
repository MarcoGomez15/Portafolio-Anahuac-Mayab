public class Autor {
    public string Nombre;
    public string Nacionalidad;

    public Autor(string nombre, string nacionalidad) {
        Nombre = nombre;
        Nacionalidad = nacionalidad;
    }

    public override string ToString() {
        return "Nombre: " + Nombre + "\n" + "Nacionalidad: " + Nacionalidad;
    }
}