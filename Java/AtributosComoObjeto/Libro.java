package Java.AtributosComoObjeto;

public class Libro {
    String titulo;
    int anioPublicacion;
    Autor autor; //Atributo que es un objeto de la clase Autor

    public Libro(String titulo, int anioPublicacion, Autor autor){
        this.titulo = titulo;
        this.anioPublicacion = anioPublicacion;
        this.autor = autor;
    }

    @Override
    public String toString(){
        return autor + "\nTitulo: " + this.titulo + "\nAño de publicacion: " + this.anioPublicacion; 
    }
}
