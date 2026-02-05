class Empleado:
    # Constructores (Simulado en Python con argumentos por defecto)
    def __init__(self, nombre="", anio_contratacion=0, salario=0.0):
        # Atributos privados (convención en Python usando _)
        self._nombre = nombre
        self._anio_contratacion = anio_contratacion
        self._salario = salario

    # Getters y Setters
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_anio_contratacion(self):
        return self._anio_contratacion

    def set_anio_contratacion(self, anio_contratacion):
        self._anio_contratacion = anio_contratacion

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario

    # Metodos
    def calcular_salario(self):
        return self._salario

    def __str__(self):
        return f"\nNombre: {self._nombre}\nAnio de Contratacion: {self._anio_contratacion}\nSalario: {self._salario}"
