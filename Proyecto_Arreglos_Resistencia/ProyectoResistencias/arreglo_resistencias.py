from resistencia import formatear_ohmios, generar_aleatoria


class ArregloResistencias:
    def __init__(self, tolerancia="Dorado"):
        self.resistencias = []
        self.tolerancia = tolerancia

    def agregar(self, resistencia):
        self.resistencias.append(resistencia)

    def limpiar(self):
        self.resistencias = []

    def cantidad(self):
        return len(self.resistencias)

    def generar_aleatorias(self, n):
        self.limpiar()
        for i in range(n):
            self.agregar(generar_aleatoria(self.tolerancia))
        return self.resistencias

    def tipo(self):
        return "Arreglo"

    def calcular_total(self):
        return 0.0

    def obtener_formula(self):
        return ""

    def total_formateado(self):
        total = self.calcular_total()
        if total >= 1000:
            return formatear_ohmios(total)
        return f"{round(total, 4)} Ω"
