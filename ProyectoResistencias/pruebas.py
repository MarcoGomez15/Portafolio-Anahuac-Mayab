import estilos
import resistencia as modulo_resistencia
from arreglo_paralelo import ArregloParalelo
from arreglo_serie import ArregloSerie
from dibujo_resistencia import DibujoResistencia
from resistencia import Resistencia

# Aquí voy guardando True o False por cada prueba que hago
resultados = []


# Compara lo que salió contra lo esperado y lo guarda en el arreglo de resultados
def verificar(nombre, obtenido, esperado):
    if obtenido == esperado:
        resultados.append(True)
        print(f"  [OK]    {nombre}")
    else:
        resultados.append(False)
        print(f"  [FALLA] {nombre}")
        print(f"          esperado: {esperado}")
        print(f"          obtenido: {obtenido}")


# Pruebas de los colores de una resistencia (R1)
def probar_requerimiento_1():
    print("\nR1. Colores de una resistencia")
    verificar("160 ohmios", Resistencia(160, "Dorado").obtener_colores(),
              ["Marrón", "Azul", "Marrón"])
    verificar("5800 ohmios", Resistencia(5800, "Dorado").obtener_colores(),
              ["Verde", "Gris", "Rojo"])
    verificar("10 ohmios (mínimo)", Resistencia(10, "Dorado").obtener_colores(),
              ["Marrón", "Negro", "Negro"])
    verificar("1000000000 ohmios (máximo)", Resistencia(1000000000, "Dorado").obtener_colores(),
              ["Marrón", "Negro", "Gris"])
    verificar("47000 ohmios", Resistencia(47000, "Dorado").obtener_colores(),
              ["Amarillo", "Violeta", "Naranja"])

    pieza = Resistencia(4700, "Plateado")
    verificar("cuarta banda de tolerancia", pieza.obtener_bandas()[3].nombre, "Plateado")
    verificar("cantidad de bandas", len(pieza.obtener_bandas()), 4)

    aproximada = Resistencia(165, "Dorado")
    verificar("165 ohmios no es exacta", aproximada.es_exacta(), False)
    verificar("165 ohmios se representa como 170", aproximada.valor_representado(), 170)

    rango = Resistencia(1000, "Dorado").rango_tolerancia()
    verificar("rango de 1000 ohmios al 5 por ciento", rango, [950.0, 1050.0])

    verificar("valor fuera de rango (9)", modulo_resistencia.valor_valido(9), False)
    verificar("valor fuera de rango (2000000000)",
              modulo_resistencia.valor_valido(2000000000), False)
    verificar("valor dentro de rango (160)", modulo_resistencia.valor_valido(160), True)


# Pruebas de la suma en serie (R2)
def probar_requerimiento_2():
    print("\nR2. Valor total en serie")
    arreglo = ArregloSerie("Dorado")
    valores = [100, 220, 330]
    for i in range(len(valores)):
        arreglo.agregar(Resistencia(valores[i], "Dorado"))
    verificar("100 + 220 + 330", arreglo.calcular_total(), 650.0)
    verificar("fórmula desarrollada", arreglo.obtener_formula(), "Rts = 100 + 220 + 330")

    vacio = ArregloSerie("Dorado")
    verificar("arreglo vacío", vacio.calcular_total(), 0.0)

    aleatorio = ArregloSerie("Dorado")
    aleatorio.generar_aleatorias(50)
    verificar("se generan 50 resistencias", aleatorio.cantidad(), 50)

    dentro_del_rango = True
    for i in range(aleatorio.cantidad()):
        if modulo_resistencia.valor_valido(aleatorio.resistencias[i].valor) == False:
            dentro_del_rango = False
    verificar("todas dentro del rango permitido", dentro_del_rango, True)


# Pruebas del cálculo en paralelo (R3)
def probar_requerimiento_3():
    print("\nR3. Valor total en paralelo")
    arreglo = ArregloParalelo("Dorado")
    valores = [100, 220, 330]
    for i in range(len(valores)):
        arreglo.agregar(Resistencia(valores[i], "Dorado"))
    verificar("1/100 + 1/220 + 1/330", round(arreglo.calcular_total(), 4), 56.8966)

    iguales = ArregloParalelo("Dorado")
    for i in range(2):
        iguales.agregar(Resistencia(1000, "Dorado"))
    verificar("dos resistencias de 1000 ohmios", iguales.calcular_total(), 500.0)

    aleatorio = ArregloParalelo("Dorado")
    aleatorio.generar_aleatorias(10)
    menor = aleatorio.resistencias[0].valor
    for i in range(aleatorio.cantidad()):
        if aleatorio.resistencias[i].valor < menor:
            menor = aleatorio.resistencias[i].valor
    verificar("el total es menor que la resistencia más pequeña",
              aleatorio.calcular_total() < menor, True)


# Revisa que serie y paralelo usen los métodos del padre y cambien la fórmula
def probar_herencia():
    print("\nHerencia del diseño")
    serie = ArregloSerie("Dorado")
    paralelo = ArregloParalelo("Dorado")
    valores = [100, 200, 400]
    for i in range(len(valores)):
        serie.agregar(Resistencia(valores[i], "Dorado"))
        paralelo.agregar(Resistencia(valores[i], "Dorado"))

    # agregar() y cantidad() no están en las clases hijas, los heredan del padre
    verificar("ArregloSerie usa los métodos heredados", serie.cantidad(), 3)
    verificar("ArregloParalelo usa los métodos heredados", paralelo.cantidad(), 3)
    verificar("tipo del arreglo en serie", serie.tipo(), "Serie")
    verificar("tipo del arreglo en paralelo", paralelo.tipo(), "Paralelo")
    verificar("el mismo método da resultados distintos",
              serie.calcular_total() != paralelo.calcular_total(), True)


# Revisa que el dibujo tenga las bandas correctas (R5)
def probar_dibujo():
    print("\nR5. Dibujo de la resistencia")
    estilos.usar_color = False
    dibujo = DibujoResistencia()

    renglones = dibujo.construir(Resistencia(160, "Dorado"))
    verificar("cantidad de renglones del dibujo", len(renglones), 6)

    ultimo = renglones[5]
    verificar("aparece el nombre Marrón", "Marrón" in ultimo, True)
    verificar("aparece el nombre Azul", "Azul" in ultimo, True)
    verificar("aparece el nombre Dorado", "Dorado" in ultimo, True)

    verificar("se dibujan 4 bandas",
              contar_bandas(dibujo, Resistencia(5800, "Plateado")), 4)
    verificar("con tolerancia Ninguno se dibujan 3 bandas",
              contar_bandas(dibujo, Resistencia(5800, "Ninguno")), 3)
    estilos.usar_color = True


# Cuenta los grupos de bloques del dibujo, o sea cuántas bandas se ven
def contar_bandas(dibujo, pieza):
    renglon = dibujo.construir(pieza)[0]
    bandas = 0
    anterior = " "
    for i in range(len(renglon)):
        if renglon[i] == "█" and anterior != "█":
            bandas = bandas + 1
        anterior = renglon[i]
    return bandas


# Corre todas las pruebas y muestra cuántas salieron bien
def main():
    print("PRUEBAS DEL PROYECTO DE ARREGLOS - RESISTENCIA ELÉCTRICA")
    probar_requerimiento_1()
    probar_requerimiento_2()
    probar_requerimiento_3()
    probar_herencia()
    probar_dibujo()

    correctas = 0
    for i in range(len(resultados)):
        if resultados[i] == True:
            correctas = correctas + 1

    print()
    print(f"Pruebas correctas: {correctas} de {len(resultados)}")
    if correctas == len(resultados):
        print("Todas las pruebas se ejecutaron correctamente.")


if __name__ == "__main__":
    main()
