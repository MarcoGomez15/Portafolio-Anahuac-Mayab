import estilos
import resistencia as modulo_resistencia
from arreglo_paralelo import ArregloParalelo
from arreglo_serie import ArregloSerie
from codigo_colores import CodigoColores
from dibujo_resistencia import DibujoResistencia
from resistencia import Resistencia

ANCHO = 64
LIMITE_TABLA = 20
MAXIMO_RESISTENCIAS = 1000
CANCELAR = -1


class MenuPrincipal:
    def __init__(self):
        self.arreglo_serie = ArregloSerie()
        self.arreglo_paralelo = ArregloParalelo()
        self.dibujo = DibujoResistencia()
        self.codigo = CodigoColores()

    def ejecutar(self):
        print(estilos.titulo("RESISTENCIA ELÉCTRICA  ·  Proyecto de arreglos", ANCHO))

        salir = False
        while salir == False:
            self.mostrar_menu()
            opcion = input("Elige una opción [1-4]: ").strip()

            if opcion == "1":
                self.opcion_colores()
            elif opcion == "2":
                self.opcion_arreglos()
            elif opcion == "3":
                self.opcion_tabla()
            elif opcion == "4":
                print(estilos.exito("\n  Programa terminado. ¡Hasta luego!\n"))
                salir = True
            else:
                print(estilos.aviso("Opción no válida: escribe un número del 1 al 4.\n"))

    def mostrar_menu(self):
        print()
        print("  1) Determinar los colores de una resistencia")
        print("  2) Calcular el total de n resistencias en serie y en paralelo")
        print("  3) Consultar la tabla del código de colores")
        print("  4) Salir")
        print(estilos.bloque("-" * ANCHO, estilos.GRIS))

    def opcion_colores(self):
        print(estilos.subtitulo("Opción 1. Colores de una resistencia", ANCHO))
        print(f"  Valores permitidos: de {modulo_resistencia.VALOR_MINIMO} a "
              f"{modulo_resistencia.VALOR_MAXIMO} ohmios.")

        valor = self.leer_entero("  Valor de la resistencia (Ω): ",
                                 modulo_resistencia.VALOR_MINIMO,
                                 modulo_resistencia.VALOR_MAXIMO)
        if valor == CANCELAR:
            return

        tolerancia = self.leer_tolerancia()
        if tolerancia == "":
            return

        pieza = Resistencia(valor, tolerancia)

        print()
        self.dibujo.mostrar(pieza)

        colores = pieza.obtener_colores()
        texto_colores = colores[0] + " → " + colores[1] + " → " + colores[2]
        rango = pieza.rango_tolerancia()

        print()
        print(f"  Valor            : {pieza.valor} Ω  ({pieza.valor_formateado()})")
        print(f"  Colores          : {estilos.texto_color(texto_colores, estilos.NARANJA, True)}")
        print(f"  Tolerancia       : {pieza.tolerancia.nombre} "
              f"(± {pieza.tolerancia.tolerancia} %)")
        print(f"  Rango real       : {round(rango[0], 2)} Ω a {round(rango[1], 2)} Ω")

        if pieza.es_exacta() == False:
            print(estilos.aviso("El código de 4 bandas solo admite dos cifras significativas, "
                                f"por lo que {pieza.valor} Ω se representa "
                                f"como {pieza.valor_representado()} Ω."))
        print()

    def opcion_arreglos(self):
        print(estilos.subtitulo("Opción 2. Arreglos en serie y en paralelo", ANCHO))
        print(f"  Cada resistencia recibe un valor aleatorio entre "
              f"{modulo_resistencia.VALOR_MINIMO} y {modulo_resistencia.VALOR_MAXIMO} ohmios.")

        cantidad = self.leer_entero("  Cantidad de resistencias (n): ", 1, MAXIMO_RESISTENCIAS)
        if cantidad == CANCELAR:
            return

        resistencias = self.arreglo_serie.generar_aleatorias(cantidad)
        self.arreglo_paralelo.limpiar()
        for i in range(len(resistencias)):
            self.arreglo_paralelo.agregar(resistencias[i])

        self.imprimir_tabla(resistencias)

        serie = estilos.texto_color(self.arreglo_serie.total_formateado(), estilos.NARANJA, True)
        paralelo = estilos.texto_color(self.arreglo_paralelo.total_formateado(),
                                       estilos.NARANJA, True)
        print()
        print(f"  Valor total en SERIE    : {serie}")
        print(f"  Valor total en PARALELO : {paralelo}")
        print()
        print(estilos.bloque("  " + self.resumir(self.arreglo_serie.obtener_formula()),
                             estilos.GRIS))
        print(estilos.bloque("  " + self.resumir(self.arreglo_paralelo.obtener_formula()),
                             estilos.GRIS))
        print()

    def imprimir_tabla(self, resistencias):
        print()
        print(f"  {'#':>4}  {'Valor (Ω)':>13}  {'Equivalente':>12}  Colores de las bandas")
        print(estilos.bloque("  " + "-" * (ANCHO - 2), estilos.GRIS))

        for i in range(len(resistencias)):
            if i == LIMITE_TABLA:
                restantes = len(resistencias) - LIMITE_TABLA
                print(estilos.bloque(f"  ... y {restantes} resistencias más.", estilos.GRIS))
                return

            pieza = resistencias[i]
            colores = pieza.obtener_colores()
            texto_colores = colores[0] + ", " + colores[1] + ", " + colores[2]
            print(f"  {i + 1:>4}  {pieza.valor:>13}  "
                  f"{pieza.valor_formateado():>12}  {texto_colores}")

    def opcion_tabla(self):
        print(estilos.subtitulo("Opción 3. Código de colores de 4 bandas", ANCHO))
        print(f"  {'Color':<10} {'':4}  {'1ra y 2da':>9}  {'3ra banda':>16}  {'4ta banda':>10}")
        print(estilos.bloque("  " + "-" * (ANCHO - 2), estilos.GRIS))

        for i in range(len(self.codigo.tabla)):
            color = self.codigo.tabla[i]
            muestra = estilos.bloque("████", color.rgb)

            digito = "—"
            if color.digito != None:
                digito = str(color.digito)

            multiplicador = "—"
            if color.multiplicador != None:
                multiplicador = "x " + str(color.multiplicador)

            tolerancia = "—"
            if color.tolerancia != None:
                tolerancia = "± " + str(color.tolerancia) + " %"

            print(f"  {color.nombre:<10} {muestra}  {digito:>9}  "
                  f"{multiplicador:>16}  {tolerancia:>10}")
        print()

    def leer_entero(self, mensaje, minimo, maximo):
        while True:
            texto = input(mensaje).strip()

            if texto.lower() == "c":
                return CANCELAR

            limpio = texto.replace(",", "").replace(" ", "")

            if limpio.isdigit() == False:
                print(estilos.aviso("Escribe un número entero (o la letra c para cancelar)."))
            elif int(limpio) < minimo or int(limpio) > maximo:
                print(estilos.aviso(f"El valor debe estar entre {minimo} y {maximo}."))
            else:
                return int(limpio)

    def leer_tolerancia(self):
        tolerancias = self.codigo.obtener_tolerancias()

        opciones = ""
        for i in range(len(tolerancias)):
            if i > 0:
                opciones = opciones + "  "
            opciones = opciones + f"{i + 1}) {tolerancias[i].nombre}"
            opciones = opciones + f" (± {tolerancias[i].tolerancia} %)"
        print("  Tolerancia →  " + opciones)

        while True:
            texto = input("  Elige la tolerancia [Enter = Dorado]: ").strip()

            if texto == "":
                return tolerancias[0].nombre
            if texto.lower() == "c":
                return ""
            if texto.isdigit() == True and int(texto) >= 1 and int(texto) <= len(tolerancias):
                return tolerancias[int(texto) - 1].nombre

            print(estilos.aviso(f"Escribe un número del 1 al {len(tolerancias)}."))

    def resumir(self, formula):
        if len(formula) <= 58:
            return formula
        return formula[0:58] + " ..."
