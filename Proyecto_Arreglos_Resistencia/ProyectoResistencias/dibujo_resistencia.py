import estilos

MARGEN = 4
LARGO_ALAMBRE = 6
ANCHO_CUERPO = 46
ANCHO_BANDA = 4

POSICIONES_BANDAS = [5, 15, 25, 37]
ETIQUETAS = ["1er díg.", "2do díg.", "multip.", "toler."]

COLOR_CUERPO = [227, 192, 141]
COLOR_ALAMBRE = [154, 153, 150]


class DibujoResistencia:
    def construir(self, resistencia):
        bandas = resistencia.obtener_bandas()
        cuerpo = self.construir_cuerpo(bandas)
        alambre = estilos.bloque("─" * LARGO_ALAMBRE, COLOR_ALAMBRE)
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

    def mostrar(self, resistencia):
        renglones = self.construir(resistencia)
        for i in range(len(renglones)):
            print(renglones[i])

    def construir_cuerpo(self, bandas):
        colores = []
        for i in range(ANCHO_CUERPO):
            colores.append(None)

        for i in range(len(bandas)):
            if bandas[i].nombre == "Ninguno":
                continue
            inicio = POSICIONES_BANDAS[i]
            for posicion in range(inicio, inicio + ANCHO_BANDA):
                colores[posicion] = bandas[i].rgb

        renglon = ""
        posicion = 0
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

    def construir_guias(self):
        centros = self.obtener_centros()
        renglon = []
        for i in range(MARGEN + LARGO_ALAMBRE + ANCHO_CUERPO):
            renglon.append(" ")
        for i in range(len(centros)):
            renglon[centros[i]] = "│"
        return estilos.bloque("".join(renglon).rstrip(), COLOR_ALAMBRE)

    def construir_etiquetas(self, textos, tenue):
        centros = self.obtener_centros()
        renglon = []
        for i in range(MARGEN + LARGO_ALAMBRE + ANCHO_CUERPO + 12):
            renglon.append(" ")

        for i in range(len(textos)):
            texto = textos[i]
            inicio = centros[i] - len(texto) // 2
            for letra in range(len(texto)):
                renglon[inicio + letra] = texto[letra]

        texto_final = "".join(renglon).rstrip()
        if tenue == True:
            return estilos.bloque(texto_final, estilos.GRIS)
        return texto_final

    def obtener_centros(self):
        centros = []
        for i in range(len(POSICIONES_BANDAS)):
            centros.append(MARGEN + LARGO_ALAMBRE + POSICIONES_BANDAS[i] + ANCHO_BANDA // 2)
        return centros
