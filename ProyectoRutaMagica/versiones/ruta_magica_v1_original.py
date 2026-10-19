"""
Ruta Magica -- Proyecto de grafos
VERSION 1 (ORIGINAL) -- SE CONSERVA SOLO COMO REFERENCIA.

Equipo: Marco Antonio Gomez Fuentes (581874), Amir Moises Hernandez Farah
(584687), Emiliano Peniche Correa (581158), Rodrigo Quijano Lopez (582035).

Este archivo contiene el codigo original sin cambios en la logica.
Los comentarios marcados con "ERROR #n" senalan cada falla encontrada
durante la revision. La correccion de cada error esta en
../ruta_magica.py y se resume en ../CAMBIOS.md.

NO usar esta version: calcula rutas incorrectas.
"""

import heapq  # ERROR #7: se importa heapq pero nunca se usa. Dijkstra necesita
              # una cola de prioridad y aqui no se implementa ninguna.

DATOS = """# Pueblos Magicos de Puebla -- Distancias en km
Zacatlan Chignahuapan 22
Zacatlan Tetela_de_Ocampo 48
Chignahuapan Tetela_de_Ocampo 42
Tetela_de_Ocampo Cuetzalan 68
Cuetzalan Tlatlauquitepec 38
Zacatlan Xicotepec 55
Xicotepec Pahuatlan 32
Pahuatlan Zacatlan 60
Chignahuapan Tlatlauquitepec 90
Xicotepec Cuetzalan 115"""

NOMBRES = {
    "Zacatlan": "Zacatlan de las Manzanas",
    "Chignahuapan": "Chignahuapan",
    "Tetela_de_Ocampo": "Tetela de Ocampo",
    "Cuetzalan": "Cuetzalan del Progreso",
    "Tlatlauquitepec": "Tlatlauquitepec",
    "Xicotepec": "Xicotepec de Juarez",
    "Pahuatlan": "Pahuatlan",
}
ORDEN = list(NOMBRES.keys())

LINEA = "=" * 64


def cargar_grafo():
    """Lee los datos y construye el grafo como lista de adyacencia."""
    grafo = {}
    for linea in DATOS.splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#"):
            continue
        partes = linea.split()
        # ERROR #9: no se valida que la linea tenga exactamente 3 partes ni que
        # el peso sea un entero no negativo. Una linea mal escrita truena el programa.
        a, b, peso = partes[0], partes[1], int(partes[2])
        grafo[a] = [(b, peso)]
        # ERROR #1: "=" REEMPLAZA la lista en cada linea. Cada pueblo se queda
        # solo con su ULTIMA conexion (Zacatlan termina conectado solo a Xicotepec).
        # ERROR #2: solo se agrega a -> b. Las carreteras son de doble sentido,
        # por lo que tambien falta b -> a (Tlatlauquitepec queda sin salidas).
    return grafo


def dijkstra(grafo, origen, destino):
    """Devuelve (camino, distancia_total) del origen al destino."""
    # ERROR #3: esto NO es Dijkstra, es una busqueda en anchura (BFS).
    # La cola es FIFO (pop(0)) y no esta ordenada por distancia acumulada,
    # asi que encuentra el camino con MENOS TRAMOS, no con MENOS KILOMETROS.
    cola = [origen]
    visitados = {origen}
    distancias = {origen: 0}
    caminos = {origen: [origen]}

    while cola:
        nodo = cola.pop(0)  # ERROR #3: FIFO; ademas pop(0) en lista es O(n).
        if nodo == destino:
            break
        for vecino, peso in grafo.get(nodo, []):
            if vecino not in visitados:
                # ERROR #3: marcar como visitado al DESCUBRIR el nodo impide
                # actualizarlo si despues aparece una ruta mas corta (no hay
                # "relajacion" de aristas).
                visitados.add(vecino)
                distancias[vecino] = distancias[nodo] + peso
                caminos[vecino] = caminos[nodo]
                # ERROR #4: esto NO copia la lista, solo crea otro nombre para
                # la MISMA lista. El append de abajo modifica tambien el camino
                # del nodo padre y todos los caminos se mezclan.
                caminos[vecino].append(vecino)
                cola.append(vecino)

    return caminos.get(destino, []), distancias.get(destino, 0)
    # ERROR #8: si no hay ruta devuelve distancia 0, que se confunde con
    # "origen igual a destino". Deberia devolver None.


def mostrar_nombre(clave):
    # (Correcto) La ruta usa nombres cortos, igual que la "Ejecucion
    # Esperada" del enunciado. No se cuenta como error.
    return clave.replace("_", " ")


def pedir_pueblo(texto):
    while True:
        try:
            opcion = int(input(f"Seleccione pueblo de {texto} (1-{len(ORDEN)}): "))
            if 1 < opcion < len(ORDEN):
                # ERROR #5: desigualdades estrictas. Rechaza las opciones 1 y 7,
                # que si son validas. Debe ser 1 <= opcion <= len(ORDEN).
                return ORDEN[opcion - 1]
        except ValueError:
            pass
        print("  Opcion invalida, intente de nuevo.")


def imprimir_resultado(grafo, camino, total):
    print()
    print(LINEA)
    if not camino:
        print("  [X] NO EXISTE RUTA ENTRE ESOS PUEBLOS")
        print(LINEA)
        return
    print("  [OK] RUTA ENCONTRADA")
    print(LINEA)
    print()
    ancho = max(len(mostrar_nombre(p)) for p in camino)
    for i in range(len(camino) - 1):
        a, b = camino[i], camino[i + 1]
        peso = grafo[a][0][1]
        # ERROR #6: toma el peso del PRIMER vecino de "a", no el del tramo a -> b.
        # Los km que se imprimen por tramo pueden ser incorrectos.
        print(f"  {mostrar_nombre(a):<{ancho}} --({peso:>3} km)--> {mostrar_nombre(b)}")
    print()
    print("  Ruta completa:")
    print("  " + " -> ".join(mostrar_nombre(p) for p in camino))
    print()
    print(f"  Distancia total: {total} km")
    print(LINEA)


def main():
    grafo = cargar_grafo()

    print(LINEA)
    print("         RUTA MAGICA -- PUEBLA")
    print("   Camino mas corto entre Pueblos Magicos")
    print(LINEA)
    print()
    print("Pueblos Magicos disponibles:")
    for i, clave in enumerate(ORDEN, start=1):
        print(f"  {i}. {NOMBRES[clave]}")
    print()

    while True:
        origen = pedir_pueblo("ORIGEN")
        print(f"  -> Origen: {NOMBRES[origen]}")
        print()
        destino = pedir_pueblo("DESTINO")
        print(f"  -> Destino: {NOMBRES[destino]}")
        print()
        print("Algoritmo utilizado: Dijkstra")
        print("Calculando ruta mas corta...")

        camino, total = dijkstra(grafo, origen, destino)
        imprimir_resultado(grafo, camino, total)

        print()
        resp = input("Desea consultar otra ruta? (S/N): ").strip().upper()
        if resp != "S":
            print("Gracias por usar Ruta Magica.")
            break
        print()


if __name__ == "__main__":
    # ERROR #10 (menor): Ctrl+C o fin de entrada muestran un traceback feo.
    main()
