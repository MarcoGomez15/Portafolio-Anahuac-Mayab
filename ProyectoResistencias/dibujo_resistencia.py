import estilos

# Medidas del dibujo, todo está en caracteres
MARGEN = 4
LARGO_ALAMBRE = 6
ANCHO_CUERPO = 46
ANCHO_BANDA = 4

# Columna donde empieza cada una de las 4 bandas
POSICIONES_BANDAS = [5, 15, 25, 37]
ETIQUETAS = ["1er díg.", "2do díg.", "multip.", "toler."]

# Colores del cuerpo y de los alambres
COLOR_CUERPO = [227, 192, 141]
COLOR_ALAMBRE = [154, 153, 150]


# Dibuja la resistencia en la terminal con sus bandas de colores
class DibujoResistencia:
    # Arma todos los renglones del dibujo y los regresa en un arreglo
    def construir(self, resistencia):
        bandas = resistencia.obtener_bandas()
        cuerpo = self.construir_cuerpo(bandas)
        alambre = estilos.bloque("─" * LARGO_ALAMBRE, COLOR_ALAMBRE, None)
        sangria = " " * (MARGEN + LARGO_ALAMBRE)

        nombres = []
        for i in range(len(bandas)):
            nombres.append(bandas[i].nombre)

        renglones = []
        renglones.append(sangria + cuerpo)
        renglones.append(" " * MARGEN + alambre + cuerpo + alambre)
        renglones.append(sangria + cuerpo)
        renglones.append(self.construir_guias())
        renglones.append(self.construir_etiquetas(ETIQUETAS, True))
        renglones.append(self.construir_etiquetas(nombres, False))
        return renglones

    # Imprime el dibujo renglón por renglón
    def mostrar(self, resistencia):
        renglones = self.construir(resistencia)
        for i in range(len(renglones)):
            print(renglones[i])

    # Arma el cuerpo de la resistencia y pinta cada banda en su posición
    def construir_cuerpo(self, bandas):
        colores = []
        for i in range(ANCHO_CUERPO):
            colores.append(None)

        for i in range(len(bandas)):
            # el color Ninguno significa que no hay cuarta banda, así que no la pinto
            if bandas[i].nombre != "Ninguno":
                inicio = POSICIONES_BANDAS[i]
                for posicion in range(inicio, inicio + ANCHO_BANDA):
                    colores[posicion] = bandas[i].rgb

        renglon = ""
        posicion = 0
        # junto los espacios seguidos del mismo color para pintarlos de una vez
        while posicion < ANCHO_CUERPO:
            color = colores[posicion]
            final = posicion
            while final < ANCHO_CUERPO and colores[final] == color:
                final = final + 1
            cantidad = final - posicion

            if color == None:
                renglon = renglon + estilos.bloque(" " * cantidad, None, COLOR_CUERPO)
            else:
                renglon = renglon + estilos.bloque("█" * cantidad, color, COLOR_CUERPO)
            posicion = final
        return renglon

    # Pone las rayitas que apuntan a cada banda
    def construir_guias(self):
        centros = self.obtener_centros()
        letras = []
        for i in range(MARGEN + LARGO_ALAMBRE + ANCHO_CUERPO):
            letras.append(" ")
        for i in range(len(centros)):
            letras[centros[i]] = "│"
        return estilos.bloque(self.unir(letras), COLOR_ALAMBRE, None)

    # Escribe un texto centrado abajo de cada banda
    def construir_etiquetas(self, textos, tenue):
        centros = self.obtener_centros()
        letras = []
        for i in range(MARGEN + LARGO_ALAMBRE + ANCHO_CUERPO + 12):
            letras.append(" ")

        for i in range(len(textos)):
            texto = textos[i]
            inicio = centros[i] - len(texto) // 2
            for letra in range(len(texto)):
                letras[inicio + letra] = texto[letra]

        renglon = self.unir(letras)
        if tenue == True:
            return estilos.bloque(renglon, estilos.GRIS, None)
        return renglon

    # Junta un arreglo de letras en un solo texto
    def unir(self, letras):
        renglon = ""
        for i in range(len(letras)):
            renglon = renglon + letras[i]
        return renglon

    # Calcula en qué columna queda el centro de cada banda
    def obtener_centros(self):
        centros = []
        for i in range(len(POSICIONES_BANDAS)):
            centros.append(MARGEN + LARGO_ALAMBRE + POSICIONES_BANDAS[i] + ANCHO_BANDA // 2)
        return centros
