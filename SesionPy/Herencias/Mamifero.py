class Mamifero:
    def __init__(self, n="", p=0.0):
        self.__nombre = n #privado
        self._peso = p #protegido
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, n):
        self.__nombre = n

    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, p):
        self._peso = p

    def __str__(self):
        return f"Mamifero\n [{self.__nombre},{self._peso} kg]"

class Gato(Mamifero):
    def __init__(self, n="", p=0.0, b=0):
        super().__init__(n, p)
        self.__bigotes = b
    
    def __str__(self): #equivalente al toString()
        return f"{super().__str__()}\n [{self.__bigotes} bigotes]"

class Vaca(Mamifero):
    def __init__(self, n="", p=0.0, l=0.0):
        super().__init__(n, p)
        self.__litros_leche = l
    
    def calcular_cantidad_comida(self):
        print(f"{self._peso * 0.03}kg de alimento")
    
    def __str__(self): #equivalente al toString()
        return f"{super().__str__()}\n [{self.__litros_leche} litros de leche]"

class Ballena(Mamifero):
    def __init__(self, n="", p=0.0):
        super().__init__(n, p)
    
    def __str__(self): #equivalente al toString()
        return f"{super().__str__()}\n [Ballena]"