import random

from codigo_colores import CodigoColores

# Rango de valores que pide el proyecto
VALOR_MINIMO = 10
VALOR_MAXIMO = 1000000000


# Una resistencia: a partir de su valor en ohmios saca los colores de sus bandas
class Resistencia:
    # Guarda el valor y busca el color de la tolerancia en la tabla
    def __init__(self, valor, tolerancia):
        self.codigo = CodigoColores()
        self.valor = valor
        self.tolerancia = self.codigo.obtener_por_nombre(tolerancia)

    # Separa el valor en sus 2 primeros dígitos y el exponente del multiplicador
    # ej. 5800 -> [5, 8, 2] porque 58 x 10^2 = 5800
    def descomponer(self):
        exponente = len(str(self.valor)) - 2
        base = 10 ** exponente
        mantisa = (self.valor + base // 2) // base

        # si al redondear sale 100 (ej. 999) lo paso a 10 y subo el exponente
        if mantisa == 100:
            mantisa = 10
            exponente = exponente + 1

        primer_digito = mantisa // 10
        segundo_digito = mantisa % 10
        return [primer_digito, segundo_digito, exponente]

    # Regresa las 4 bandas: dígito 1, dígito 2, multiplicador y tolerancia
    def obtener_bandas(self):
        datos = self.descomponer()
        bandas = []
        bandas.append(self.codigo.obtener_por_digito(datos[0]))
        bandas.append(self.codigo.obtener_por_digito(datos[1]))
        bandas.append(self.codigo.obtener_por_multiplicador(datos[2]))
        bandas.append(self.tolerancia)
        return bandas

    # Regresa los nombres de los 3 primeros colores, que es lo que pide el R1
    def obtener_colores(self):
        bandas = self.obtener_bandas()
        colores = []
        for i in range(3):
            colores.append(bandas[i].nombre)
        return colores

    # Calcula el valor que de verdad marcan los colores
    def valor_representado(self):
        datos = self.descomponer()
        return (datos[0] * 10 + datos[1]) * (10 ** datos[2])

    # Revisa si el valor se puede representar exacto con solo 2 dígitos
    def es_exacta(self):
        return self.valor_representado() == self.valor

    # Saca el valor mínimo y máximo según el porcentaje de tolerancia
    def rango_tolerancia(self):
        margen = self.valor * self.tolerancia.tolerancia / 100
        return [self.valor - margen, self.valor + margen]

    # Regresa el valor con sus unidades para que se lea mejor
    def valor_formateado(self):
        return formatear_ohmios(self.valor)


# Convierte los ohmios a kΩ, MΩ o GΩ según qué tan grande sea el número
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


# Revisa que el valor esté dentro del rango permitido
def valor_valido(valor):
    if valor < VALOR_MINIMO:
        return False
    if valor > VALOR_MAXIMO:
        return False
    return True


# Crea una resistencia con un valor al azar dentro del rango
def generar_aleatoria(tolerancia):
    valor = random.randint(VALOR_MINIMO, VALOR_MAXIMO)
    return Resistencia(valor, tolerancia)
