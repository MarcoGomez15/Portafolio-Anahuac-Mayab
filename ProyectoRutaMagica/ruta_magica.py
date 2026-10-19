"""
Ruta Magica -- Camino mas corto entre Pueblos Magicos de Puebla
===============================================================
Proyecto de grafos

Equipo:
  Marco Antonio Gomez Fuentes   581874
  Amir Moises Hernandez Farah   584687
  Emiliano Peniche Correa       581158
  Rodrigo Quijano Lopez         582035

Version: 2.0 (corregida)

Modelo del problema
-------------------
Los Pueblos Magicos de la Sierra Norte de Puebla forman un GRAFO PONDERADO
NO DIRIGIDO:
  - Vertices: los 7 pueblos.
  - Aristas:  las 10 carreteras que los conectan directamente. Son de doble
              sentido, por eso el grafo es no dirigido.
  - Pesos:    distancia por carretera en kilometros.

Representacion: lista de adyacencia (dict de diccionarios), recomendada en el
enunciado para grafos dispersos: 7 vertices con solo 10 de 21 aristas posibles.

Justificacion del algoritmo: DIJKSTRA
-------------------------------------
  - Todas las distancias son positivas, que es la unica condicion que
    Dijkstra necesita.
  - Cada consulta va de UN origen a UN destino (origen unico).
  - Floyd-Warshall calcula la distancia entre TODOS los pares de pueblos con
    una matriz V x V: es trabajo de mas para una sola consulta, O(V^3).
  - Bellman-Ford solo hace falta con pesos negativos, que en kilometros no
    existen, y es mas lento: O(V * E).
  - Dijkstra con cola de prioridad (heapq) es O((V + E) log V), el mas
    eficiente de los tres para este caso.

Los comentarios "[Corrige ERROR #n]" indican que parte del codigo reemplaza
cada falla de la version 1 (ver versiones/ y CAMBIOS.md).

Ejecucion:  python ruta_magica.py
Pruebas:    python test_ruta_magica.py
"""

import heapq
from pathlib import Path

# ---------------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------------

# Archivo con las conexiones (formato del enunciado), junto a este script.
ARCHIVO_DATOS = Path(__file__).with_name("pueblos.txt")

# Clave del archivo -> nombre completo para el menu.
NOMBRES = {
    "Zacatlan": "Zacatlan de las Manzanas",
    "Chignahuapan": "Chignahuapan",
    "Tetela_de_Ocampo": "Tetela de Ocampo",
    "Cuetzalan": "Cuetzalan del Progreso",
    "Tlatlauquitepec": "Tlatlauquitepec",
    "Xicotepec": "Xicotepec de Juarez",
    "Pahuatlan": "Pahuatlan",
}
ORDEN = list(NOMBRES.keys())  # orden del menu (igual al del enunciado)

LINEA = "=" * 64
INFINITO = float("inf")


# ---------------------------------------------------------------------------
# Construccion del grafo
# ---------------------------------------------------------------------------

def cargar_grafo(texto):
    """
    Construye el grafo como lista de adyacencia: {pueblo: {vecino: km}}.

    Un diccionario de vecinos (en lugar de una lista de tuplas) permite
    consultar el peso de una arista directamente con grafo[a][b].
    """
    grafo = {clave: {} for clave in NOMBRES}

    for num, linea in enumerate(texto.splitlines(), start=1):
        linea = linea.strip()
        if not linea or linea.startswith("#"):
            continue  # ignora lineas vacias y comentarios

        partes = linea.split()
        # [Corrige ERROR #9] Validar el formato antes de usar los datos.
        if len(partes) != 3:
            raise ValueError(f"Linea {num} mal formada: {linea!r}")
        a, b, peso_txt = partes
        # isdigit() rechaza negativos: Dijkstra no admite pesos negativos.
        if not peso_txt.isdigit():
            raise ValueError(f"Linea {num}: la distancia debe ser un entero >= 0")
        peso = int(peso_txt)

        # [Corrige ERROR #1] Se AGREGA el vecino al diccionario existente
        #   en lugar de reemplazar toda la lista.
        # [Corrige ERROR #2] La arista se registra en ambos sentidos porque
        #   las carreteras son de doble sentido (grafo no dirigido).
        grafo.setdefault(a, {})[b] = peso
        grafo.setdefault(b, {})[a] = peso

    return grafo


def leer_datos(ruta=ARCHIVO_DATOS):
    """Lee el archivo de datos y devuelve su texto."""
    return Path(ruta).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Algoritmo de Dijkstra
# ---------------------------------------------------------------------------

def dijkstra(grafo, origen):
    """
    Ejecuta Dijkstra desde `origen`.

    Devuelve:
      distancias: {pueblo: km minimos desde origen}  (INFINITO si no hay ruta)
      previo:     {pueblo: pueblo anterior en la ruta mas corta}

    [Corrige ERROR #3 y #7] Dijkstra real con cola de prioridad (heapq):
      siempre se procesa primero el pueblo con MENOR distancia acumulada y
      cada arista se "relaja" (se actualiza si se encontro una ruta mas
      corta). Asi se minimizan los kilometros, no el numero de tramos.
    """
    distancias = {pueblo: INFINITO for pueblo in grafo}
    distancias[origen] = 0
    previo = {}
    cola = [(0, origen)]          # (distancia acumulada, pueblo)
    visitados = set()

    while cola:
        dist, nodo = heapq.heappop(cola)   # el de menor distancia
        if nodo in visitados:
            continue                        # entrada vieja en la cola
        visitados.add(nodo)                 # su distancia ya es definitiva

        for vecino, peso in grafo[nodo].items():
            nueva = dist + peso
            if nueva < distancias[vecino]:  # relajacion de la arista
                distancias[vecino] = nueva
                previo[vecino] = nodo
                heapq.heappush(cola, (nueva, vecino))

    return distancias, previo


def reconstruir_camino(previo, origen, destino):
    """
    Recorre los predecesores desde el destino hasta el origen.

    [Corrige ERROR #4] En vez de copiar listas en cada paso (lo que hacia
    que varias rutas compartieran la misma lista), se guarda solo el
    predecesor de cada pueblo y el camino se arma al final.
    """
    camino = [destino]
    while camino[-1] != origen:
        camino.append(previo[camino[-1]])
    camino.reverse()
    return camino


def ruta_mas_corta(grafo, origen, destino):
    """
    Devuelve (camino, distancia_total).

    [Corrige ERROR #8] Si no existe ruta devuelve ([], None), para no
    confundirlo con distancia 0 (origen igual a destino).
    """
    distancias, previo = dijkstra(grafo, origen)
    if distancias[destino] == INFINITO:
        return [], None
    return reconstruir_camino(previo, origen, destino), distancias[destino]


# ---------------------------------------------------------------------------
# Entrada y salida (formato de la "Ejecucion Esperada" del enunciado)
# ---------------------------------------------------------------------------

def mostrar_nombre(clave):
    """Nombre corto para la ruta, como en el enunciado: 'Tetela de Ocampo'."""
    return clave.replace("_", " ")


def pedir_pueblo(texto):
    """Pide un numero de pueblo hasta que sea valido y devuelve su clave."""
    while True:
        try:
            opcion = int(input(f" Seleccione pueblo de {texto} (1-{len(ORDEN)}): "))
            # [Corrige ERROR #5] Rango inclusivo: 1 y 7 tambien son validos.
            if 1 <= opcion <= len(ORDEN):
                return ORDEN[opcion - 1]
        except ValueError:
            pass
        print("   Opcion invalida, intente de nuevo.")


def imprimir_resultado(grafo, camino, total):
    print()
    print(LINEA)
    if not camino:
        print("   [X] NO EXISTE RUTA ENTRE ESOS PUEBLOS")
        print(LINEA)
        return

    print("   [OK] RUTA ENCONTRADA")
    print(LINEA)
    print()
    if len(camino) == 1:
        print("   El origen y el destino son el mismo pueblo.")
    else:
        tramos = list(zip(camino, camino[1:]))
        ancho = max(len(mostrar_nombre(a)) for a, _ in tramos)
        # [Corrige ERROR #6] Peso exacto del tramo a -> b.
        ancho_km = max(len(str(grafo[a][b])) for a, b in tramos)
        for a, b in tramos:
            peso = grafo[a][b]
            print(f"   {mostrar_nombre(a):<{ancho}} --({peso:>{ancho_km}} km)--> "
                  f"{mostrar_nombre(b)}")
    print()
    print("   Ruta completa:")
    print("   " + " -> ".join(mostrar_nombre(p) for p in camino))
    print()
    print(f"   Distancia total: {total} km")
    print(LINEA)


def main():
    grafo = cargar_grafo(leer_datos())

    print(LINEA)
    print("         RUTA MAGICA -- PUEBLA")
    print("    Camino mas corto entre Pueblos Magicos")
    print(LINEA)
    print()
    print(" Pueblos Magicos disponibles:")
    for i, clave in enumerate(ORDEN, start=1):
        print(f"   {i}. {NOMBRES[clave]}")
    print()

    primera = True
    while True:
        origen = pedir_pueblo("ORIGEN")
        print(f"   -> Origen: {NOMBRES[origen]}")
        print()
        destino = pedir_pueblo("DESTINO")
        print(f"   -> Destino: {NOMBRES[destino]}")
        print()
        if primera:  # el enunciado lo muestra solo en la primera consulta
            print(" Algoritmo utilizado: Dijkstra")
            primera = False
        print(" Calculando ruta mas corta...")

        camino, total = ruta_mas_corta(grafo, origen, destino)
        imprimir_resultado(grafo, camino, total)

        print()
        resp = input(" Desea consultar otra ruta? (S/N): ").strip().upper()
        if resp != "S":
            print(" Gracias por usar Ruta Magica.")
            break
        print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # [Corrige ERROR #10] Salida limpia con Ctrl+C o fin de entrada.
        print("\n Programa terminado por el usuario.")
    except FileNotFoundError:
        print(f" No se encontro el archivo de datos: {ARCHIVO_DATOS}")
