#include "../ArchivosDeEncabezado/Biblioteca.h"
#include <string>
#include <iostream>
using namespace std;

Autor::Autor(string nombre, string nacionalidad){
    this->nombre = nombre;
    this->nacionalidad = nacionalidad;
}

string Autor::toString(){
    return "Nombre: " + this->nombre + "\n" + "Nacionalidad: " + this->nacionalidad;
}

Libro::Libro(string titulo, int anioPublicacion, Autor autor) : autor(autor) {
    this->titulo = titulo;
    this->anioPublicacion = anioPublicacion;
}

string Libro::toString(){
    return autor.toString() + "\nTitulo: " + this->titulo + "\nAño de publicacion: " + to_string(this->anioPublicacion);
}