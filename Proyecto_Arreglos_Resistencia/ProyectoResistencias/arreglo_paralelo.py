from arreglo_resistencias import ArregloResistencias


class ArregloParalelo(ArregloResistencias):
    def tipo(self):
        return "Paralelo"

    def calcular_total(self):
        if len(self.resistencias) == 0:
            return 0.0

        suma_inversos = 0.0
        for i in range(len(self.resistencias)):
            suma_inversos = suma_inversos + 1 / self.resistencias[i].valor
        return 1 / suma_inversos

    def obtener_formula(self):
        if len(self.resistencias) == 0:
            return "1/Rtp = 0"

        formula = "1/Rtp = "
        for i in range(len(self.resistencias)):
            if i > 0:
                formula = formula + " + "
            formula = formula + "1/" + str(self.resistencias[i].valor)
        return formula
