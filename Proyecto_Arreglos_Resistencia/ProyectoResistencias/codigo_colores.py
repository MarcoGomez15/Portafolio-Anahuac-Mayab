class BandaColor:
    def __init__(self, nombre, rgb, digito, multiplicador, tolerancia):
        self.nombre = nombre
        self.rgb = rgb
        self.digito = digito
        self.multiplicador = multiplicador
        self.tolerancia = tolerancia


class CodigoColores:
    def __init__(self):
        self.tabla = []
        self.tabla.append(BandaColor("Negro", [0, 0, 0], 0, 1, None))
        self.tabla.append(BandaColor("Marrón", [139, 69, 19], 1, 10, None))
        self.tabla.append(BandaColor("Rojo", [224, 27, 36], 2, 100, None))
        self.tabla.append(BandaColor("Naranja", [255, 120, 0], 3, 1000, None))
        self.tabla.append(BandaColor("Amarillo", [246, 211, 45], 4, 10000, None))
        self.tabla.append(BandaColor("Verde", [46, 194, 126], 5, 100000, None))
        self.tabla.append(BandaColor("Azul", [28, 113, 216], 6, 1000000, None))
        self.tabla.append(BandaColor("Violeta", [145, 65, 172], 7, 10000000, None))
        self.tabla.append(BandaColor("Gris", [119, 118, 123], 8, 100000000, None))
        self.tabla.append(BandaColor("Blanco", [255, 255, 255], 9, 1000000000, None))
        self.tabla.append(BandaColor("Dorado", [201, 162, 39], None, 0.1, 5))
        self.tabla.append(BandaColor("Plateado", [192, 192, 192], None, 0.01, 10))
        self.tabla.append(BandaColor("Ninguno", [214, 199, 161], None, None, 20))

    def obtener_por_digito(self, digito):
        for i in range(len(self.tabla)):
            if self.tabla[i].digito == digito:
                return self.tabla[i]
        return None

    def obtener_por_multiplicador(self, exponente):
        multiplicador = 10 ** exponente
        for i in range(len(self.tabla)):
            if self.tabla[i].multiplicador == multiplicador:
                return self.tabla[i]
        return None

    def obtener_por_nombre(self, nombre):
        for i in range(len(self.tabla)):
            if self.tabla[i].nombre == nombre:
                return self.tabla[i]
        return None

    def obtener_tolerancias(self):
        tolerancias = []
        for i in range(len(self.tabla)):
            if self.tabla[i].tolerancia != None:
                tolerancias.append(self.tabla[i])
        return tolerancias
