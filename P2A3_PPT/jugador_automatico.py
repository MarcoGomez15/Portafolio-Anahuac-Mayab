import random
from jugador import Jugador

class JugadorAutomatico(Jugador):
    def hacer_eleccion(self):
        opciones = ["piedra", "papel", "tijera"]
        self.eleccion = random.choice(opciones)
        return self.eleccion
