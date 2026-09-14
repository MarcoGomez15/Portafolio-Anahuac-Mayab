from arreglo_resistencias import ArregloResistencias


class ArregloSerie(ArregloResistencias):
    def tipo(self):
        return "Serie"

    def calcular_total(self):
        total = 0.0
        for i in range(len(self.resistencias)):
            total = total + self.resistencias[i].valor
        return total

    def obtener_formula(self):
        if len(self.resistencias) == 0:
            return "Rts = 0"

        formula = "Rts = "
        for i in range(len(self.resistencias)):
            if i > 0:
                formula = formula + " + "
            formula = formula + str(self.resistencias[i].valor)
        return formula
