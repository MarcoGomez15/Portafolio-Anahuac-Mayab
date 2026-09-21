from resistencia import formatear_ohmios, generar_aleatoria


# Clase padre: guarda las resistencias en un arreglo.
# ArregloSerie y ArregloParalelo heredan de esta clase
class ArregloResistencias:
    # Empieza con el arreglo vacío
    def __init__(self, tolerancia):
        self.resistencias = []
        self.tolerancia = tolerancia

    # Agrega una resistencia al final del arreglo
    def agregar(self, resistencia):
        self.resistencias.append(resistencia)

    # Deja el arreglo vacío
    def limpiar(self):
        self.resistencias = []

    # Regresa cuántas resistencias hay en el arreglo (n)
    def cantidad(self):
        return len(self.resistencias)

    # Llena el arreglo con n resistencias de valor aleatorio
    def generar_aleatorias(self, n):
        self.limpiar()
        for i in range(n):
            self.agregar(generar_aleatoria(self.tolerancia))
        return self.resistencias

    # Nombre del tipo de arreglo, cada clase hija pone el suyo
    def tipo(self):
        return "Arreglo"

    # Cada clase hija cambia este método con su propia fórmula
    def calcular_total(self):
        return 0.0

    # Regresa la fórmula con los valores, también la cambian las hijas
    def obtener_formula(self):
        return ""

    # Regresa el total ya con sus unidades
    def total_formateado(self):
        total = self.calcular_total()
        if total >= 1000:
            return formatear_ohmios(total)
        return f"{round(total, 4)} Ω"
