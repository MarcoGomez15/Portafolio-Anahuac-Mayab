import estilos
import resistencia as modulo_resistencia
from arreglo_paralelo import ArregloParalelo
from arreglo_resistencias import ArregloResistencias
from arreglo_serie import ArregloSerie
from dibujo_resistencia import DibujoResistencia
from resistencia import Resistencia

pruebas_totales = 0
pruebas_correctas = 0


def verificar(nombre, obtenido, esperado):
    global pruebas_totales, pruebas_correctas
    pruebas_totales = pruebas_totales + 1

    if obtenido == esperado:
        pruebas_correctas = pruebas_correctas + 1
        print(f"  [OK]    {nombre}")
    else:
        print(f"  [FALLA] {nombre}")
        print(f"          esperado: {esperado}")
        print(f"          obtenido: {obtenido}")


def probar_requerimiento_1():
    print("\nR1. Colores de una resistencia")
    verificar("160 ohmios", Resistencia(160).obtener_colores(),
              ["Marrón", "Azul", "Marrón"])
    verificar("5800 ohmios", Resistencia(5800).obtener_colores(),
              ["Verde", "Gris", "Rojo"])
    verificar("10 ohmios (mínimo)", Resistencia(10).obtener_colores(),
              ["Marrón", "Negro", "Negro"])
    verificar("1000000000 ohmios (máximo)", Resistencia(1000000000).obtener_colores(),
              ["Marrón", "Negro", "Gris"])
    verificar("47000 ohmios", Resistencia(47000).obtener_colores(),
              ["Amarillo", "Violeta", "Naranja"])

    pieza = Resistencia(4700, "Plateado")
    verificar("cuarta banda de tolerancia", pieza.obtener_bandas()[3].nombre, "Plateado")
    verificar("cantidad de bandas", len(pieza.obtener_bandas()), 4)

    aproximada = Resistencia(165)
    verificar("165 ohmios no es exacta", aproximada.es_exacta(), False)
    verificar("165 ohmios se representa como 170", aproximada.valor_representado(), 170)

    rango = Resistencia(1000, "Dorado").rango_tolerancia()
    verificar("rango de 1000 ohmios al 5 por ciento", rango, [950.0, 1050.0])

    verificar("valor fuera de rango (9)", modulo_resistencia.valor_valido(9), False)
    verificar("valor fuera de rango (2000000000)",
              modulo_resistencia.valor_valido(2000000000), False)
    verificar("valor dentro de rango (160)", modulo_resistencia.valor_valido(160), True)


def probar_requerimiento_2():
    print("\nR2. Valor total en serie")
    arreglo = ArregloSerie()
    valores = [100, 220, 330]
    for i in range(len(valores)):
        arreglo.agregar(Resistencia(valores[i]))
    verificar("100 + 220 + 330", arreglo.calcular_total(), 650.0)
    verificar("fórmula desarrollada", arreglo.obtener_formula(), "Rts = 100 + 220 + 330")

    vacio = ArregloSerie()
    verificar("arreglo vacío", vacio.calcular_total(), 0.0)

    aleatorio = ArregloSerie()
    aleatorio.generar_aleatorias(50)
    verificar("se generan 50 resistencias", aleatorio.cantidad(), 50)

    dentro_del_rango = True
    for i in range(aleatorio.cantidad()):
        if modulo_resistencia.valor_valido(aleatorio.resistencias[i].valor) == False:
            dentro_del_rango = False
    verificar("todas dentro del rango permitido", dentro_del_rango, True)


def probar_requerimiento_3():
    print("\nR3. Valor total en paralelo")
    arreglo = ArregloParalelo()
    valores = [100, 220, 330]
    for i in range(len(valores)):
        arreglo.agregar(Resistencia(valores[i]))
    verificar("1/100 + 1/220 + 1/330", round(arreglo.calcular_total(), 4), 56.8966)

    iguales = ArregloParalelo()
    for i in range(2):
        iguales.agregar(Resistencia(1000))
    verificar("dos resistencias de 1000 ohmios", iguales.calcular_total(), 500.0)

    aleatorio = ArregloParalelo()
    aleatorio.generar_aleatorias(10)
    menor = aleatorio.resistencias[0].valor
    for i in range(aleatorio.cantidad()):
        if aleatorio.resistencias[i].valor < menor:
            menor = aleatorio.resistencias[i].valor
    verificar("el total es menor que la resistencia más pequeña",
              aleatorio.calcular_total() < menor, True)


def probar_herencia():
    print("\nHerencia del diseño")
    serie = ArregloSerie()
    paralelo = ArregloParalelo()
    valores = [100, 200, 400]
    for i in range(len(valores)):
        serie.agregar(Resistencia(valores[i]))
        paralelo.agregar(Resistencia(valores[i]))

    verificar("ArregloSerie hereda de ArregloResistencias",
              isinstance(serie, ArregloResistencias), True)
    verificar("ArregloParalelo hereda de ArregloResistencias",
              isinstance(paralelo, ArregloResistencias), True)
    verificar("tipo del arreglo en serie", serie.tipo(), "Serie")
    verificar("tipo del arreglo en paralelo", paralelo.tipo(), "Paralelo")
    verificar("el mismo método da resultados distintos",
              serie.calcular_total() != paralelo.calcular_total(), True)
    verificar("las clases hijas usan el método heredado cantidad()",
              serie.cantidad(), paralelo.cantidad())


def probar_dibujo():
    print("\nR5. Dibujo de la resistencia")
    estilos.activar_color(False)
    dibujo = DibujoResistencia()

    renglones = dibujo.construir(Resistencia(160, "Dorado"))
    verificar("cantidad de renglones del dibujo", len(renglones), 6)

    ultimo = renglones[5]
    verificar("aparece el nombre Marrón", "Marrón" in ultimo, True)
    verificar("aparece el nombre Azul", "Azul" in ultimo, True)
    verificar("aparece el nombre Dorado", "Dorado" in ultimo, True)

    verificar("se dibujan 4 bandas", contar_bandas(dibujo, Resistencia(5800, "Plateado")), 4)
    verificar("con tolerancia Ninguno se dibujan 3 bandas",
              contar_bandas(dibujo, Resistencia(5800, "Ninguno")), 3)
    estilos.activar_color(True)


def contar_bandas(dibujo, pieza):
    renglon = dibujo.construir(pieza)[0]
    partes = renglon.split(" ")
    bandas = 0
    for i in range(len(partes)):
        if partes[i].startswith("█") == True:
            bandas = bandas + 1
    return bandas


def main():
    print("PRUEBAS DEL PROYECTO DE ARREGLOS - RESISTENCIA ELÉCTRICA")
    probar_requerimiento_1()
    probar_requerimiento_2()
    probar_requerimiento_3()
    probar_herencia()
    probar_dibujo()

    print()
    print(f"Pruebas correctas: {pruebas_correctas} de {pruebas_totales}")
    if pruebas_correctas == pruebas_totales:
        print("Todas las pruebas se ejecutaron correctamente.")


if __name__ == "__main__":
    main()
