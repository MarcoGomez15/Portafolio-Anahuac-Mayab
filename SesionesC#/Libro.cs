using System;

public class Libro {
    public string titulo;
    public int anioPublicacion;
    public Autor autor; //Atributo que es un objeto de la clase Autor

    public Libro(string titulo, int anioPublicacion, Autor autor){
        this.titulo = titulo;
        this.anioPublicacion = anioPublicacion;
        this.autor = autor;
    }

    public override string ToString(){
        return autor + "\nTitulo: " + this.titulo + "\nAño de publicacion: " + this.anioPublicacion; 
    }
}
