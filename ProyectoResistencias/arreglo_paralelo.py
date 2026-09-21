from arreglo_resistencias import ArregloResistencias


# Resistencias conectadas en paralelo, hereda de ArregloResistencias
class ArregloParalelo(ArregloResistencias):
    # Regresa el tipo de arreglo
    def tipo(self):
        return "Paralelo"

    # Suma los inversos de cada resistencia y el total es el inverso de esa suma
    # 1/Rtp = 1/R1 + 1/R2 + ... + 1/Rn
    def calcular_total(self):
        if len(self.resistencias) == 0:
            return 0.0

        suma_inversos = 0.0
        for i in range(len(self.resistencias)):
            suma_inversos = suma_inversos + 1 / self.resistencias[i].valor
        return 1 / suma_inversos

    # Arma el texto de la fórmula con los valores del arreglo
    def obtener_formula(self):
        if len(self.resistencias) == 0:
            return "1/Rtp = 0"

        formula = "1/Rtp = "
        for i in range(len(self.resistencias)):
            if i > 0:
                formula = formula + " + "
            formula = formula + "1/" + str(self.resistencias[i].valor)
        return formula
