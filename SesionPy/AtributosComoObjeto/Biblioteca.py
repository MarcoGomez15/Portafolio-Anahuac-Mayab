class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Nombre: {self.nombre}\nNacionalidad: {self.nacionalidad}"

class Libro:
    def __init__(self, titulo, anioPublicacion, autor):
        self.titulo = titulo
        self.anioPublicacion = anioPublicacion
        self.autor = autor

    def __str__(self):
        return f"Titulo: {self.titulo}\nAño de publicacion: {self.anioPublicacion}\n{self.autor}"