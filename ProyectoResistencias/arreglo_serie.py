from arreglo_resistencias import ArregloResistencias


# Resistencias conectadas en serie, hereda de ArregloResistencias
class ArregloSerie(ArregloResistencias):
    # Regresa el tipo de arreglo
    def tipo(self):
        return "Serie"

    # Suma todas las resistencias del arreglo: Rts = R1 + R2 + ... + Rn
    def calcular_total(self):
        total = 0.0
        for i in range(len(self.resistencias)):
            total = total + self.resistencias[i].valor
        return total

    # Arma el texto de la fórmula con los valores del arreglo
    def obtener_formula(self):
        if len(self.resistencias) == 0:
            return "Rts = 0"

        formula = "Rts = "
        for i in range(len(self.resistencias)):
            if i > 0:
                formula = formula + " + "
            formula = formula + str(self.resistencias[i].valor)
        return formula
