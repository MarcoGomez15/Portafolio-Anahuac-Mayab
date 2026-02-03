class Usuario:

    # Declaración de los atributos es en el método __init__
    def __init__(self, n="", a="", e=0):
        self.__nombre = n
        self.__apellidos = a
        self.__edad = e

    # Declaracion de setter y getter
    # Python exige que se programe los getter con @property
    @property
    def nombre(self): #get de nombre
        return self.__nombre
    @nombre.setter #set de nombre
    def nombre(self, n):
        self.__nombre = n
    @property
    def apellidos(self): #get de apellidos
        return self.__apellidos
    @apellidos.setter #set de apellidos
    def apellidos(self, a):
        self.__apellidos =a
    @property
    def edad(self): #get de edad
        return self.__edad
    @edad.setter #set de edad
    def edad(self, e):
        self.__edad = e

    def iniciarSesion(self):
        print("El usuario ", self.nombre, " esta iniciando sesión.")

    def cerrarSesion(self):
        print("El usuario ", self.nombre, " ha cerrando la sesión.")

    def hacerReporte(self):
        print("Reporte de usuario")
        print("Nombre completo: ", self.nombre, " ", self.apellidos)
        print("Edad: ", self.edad)