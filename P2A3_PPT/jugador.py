class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.eleccion = ""

    def hacer_eleccion(self):
        raise NotImplementedError("Este método debe ser sobreescrito en las clases hijas")
