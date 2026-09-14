import random

from codigo_colores import CodigoColores

VALOR_MINIMO = 10
VALOR_MAXIMO = 1000000000


class Resistencia:
    def __init__(self, valor, tolerancia="Dorado"):
        self.codigo = CodigoColores()
        self.valor = valor
        self.tolerancia = self.codigo.obtener_por_nombre(tolerancia)

    def descomponer(self):
        exponente = len(str(self.valor)) - 2
        base = 10 ** exponente
        mantisa = (self.valor + base // 2) // base

        if mantisa == 100:
            mantisa = 10
            exponente = exponente + 1

        primer_digito = mantisa // 10
        segundo_digito = mantisa % 10
        return [primer_digito, segundo_digito, exponente]

    def obtener_bandas(self):
        datos = self.descomponer()
        bandas = []
        bandas.append(self.codigo.obtener_por_digito(datos[0]))
        bandas.append(self.codigo.obtener_por_digito(datos[1]))
        bandas.append(self.codigo.obtener_por_multiplicador(datos[2]))
        bandas.append(self.tolerancia)
        return bandas

    def obtener_colores(self):
        bandas = self.obtener_bandas()
        colores = []
        for i in range(3):
            colores.append(bandas[i].nombre)
        return colores

    def valor_representado(self):
        datos = self.descomponer()
        return (datos[0] * 10 + datos[1]) * (10 ** datos[2])

    def es_exacta(self):
        return self.valor_representado() == self.valor

    def rango_tolerancia(self):
        margen = self.valor * self.tolerancia.tolerancia / 100
        return [self.valor - margen, self.valor + margen]

    def valor_formateado(self):
        return formatear_ohmios(self.valor)


def formatear_ohmios(valor):
    cantidad = valor
    simbolo = "Ω"

    if valor >= 1000000000:
        cantidad = valor / 1000000000
        simbolo = "GΩ"
    elif valor >= 1000000:
        cantidad = valor / 1000000
        simbolo = "MΩ"
    elif valor >= 1000:
        cantidad = valor / 1000
        simbolo = "kΩ"

    if cantidad == int(cantidad):
        return f"{int(cantidad)} {simbolo}"
    return f"{round(cantidad, 3)} {simbolo}"


def valor_valido(valor):
    if valor < VALOR_MINIMO:
        return False
    if valor > VALOR_MAXIMO:
        return False
    return True


def generar_aleatoria(tolerancia="Dorado"):
    valor = random.randint(VALOR_MINIMO, VALOR_MAXIMO)
    return Resistencia(valor, tolerancia)
