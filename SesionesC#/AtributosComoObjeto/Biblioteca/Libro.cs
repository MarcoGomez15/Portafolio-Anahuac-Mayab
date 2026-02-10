public class Libro {
    public string Titulo;
    public int AnioPublicacion;
    public Autor Autor;

    public Libro(string titulo, int anioPublicacion, Autor autor) {
        Titulo = titulo;
        AnioPublicacion = anioPublicacion;
        Autor = autor;
    }

    public override string ToString() {
        return Autor.ToString() + "\nTitulo: " + Titulo + "\nAño de publicacion: " + AnioPublicacion;
    }
}