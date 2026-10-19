"""
Ruta Magica -- Camino mas corto entre Pueblos Magicos de Puebla
===============================================================

Autor:     Marco Antonio Gomez Fuentes
Matricula: 581874
Version:   2.0 (corregida)

Descripcion
-----------
Modela los Pueblos Magicos de Puebla como un GRAFO PONDERADO NO DIRIGIDO:
  - Vertices: pueblos.
  - Aristas:  carreteras entre pueblos (se recorren en ambos sentidos).
  - Pesos:    distancia en kilometros.

Con el algoritmo de Dijkstra calcula la ruta de menor distancia entre
dos pueblos elegidos por el usuario.

Los comentarios "[Corrige ERROR #n]" indican que parte del codigo
reemplaza cada falla de la version 1 (ver versiones/ y CAMBIOS.md).

Ejecucion:  python ruta_magica.py
Pruebas:    python test_ruta_magica.py
"""

import heapq
from pathlib import Path

# ---------------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------------

# Archivo con las conexiones, ubicado junto a este script.
ARCHIVO_DATOS = Path(__file__).with_name("pueblos.txt")

# Clave interna (sin espacios) -> nombre completo para mostrar.
NOMBRES = {
    "Zacatlan": "Zacatlan de las Manzanas",
    "Chignahuapan": "Chignahuapan",
    "Tetela_de_Ocampo": "Tetela de Ocampo",
    "Cuetzalan": "Cuetzalan del Progreso",
    "Tlatlauquitepec": "Tlatlauquitepec",
    "Xicotepec": "Xicotepec de Juarez",
    "Pahuatlan": "Pahuatlan",
}
ORDEN = list(NOMBRES.keys())  # orden en que aparecen en el menu

LINEA = "=" * 64
INFINITO = float("inf")


# ---------------------------------------------------------------------------
# Construccion del grafo
# ---------------------------------------------------------------------------

def cargar_grafo(texto):
    """
    Construye el grafo como lista de adyacencia: {pueblo: {vecino: km}}.

    Usar un diccionario de vecinos (en lugar de una lista de tuplas) permite
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

def dijkstra_completo(grafo, origen):
    """
    Ejecuta Dijkstra desde `origen` hacia todos los vertices.

    Devuelve:
      distancias: {pueblo: km minimos desde origen}  (INFINITO si no hay ruta)
      previo:     {pueblo: pueblo anterior en la ruta mas corta}

    [Corrige ERROR #3 y #7] Dijkstra real con cola de prioridad (heapq):
      siempre se procesa primero el pueblo con MENOR distancia acumulada,
      y cada arista se "relaja" (se actualiza si se encontro una ruta mas
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

    [Corrige ERROR #4] En vez de copiar listas en cada paso (lo que causaba
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
    distancias, previo = dijkstra_completo(grafo, origen)
    if distancias[destino] == INFINITO:
        return [], None
    return reconstruir_camino(previo, origen, destino), distancias[destino]


# ---------------------------------------------------------------------------
# Entrada y salida
# ---------------------------------------------------------------------------

def mostrar_nombre(clave):
    """[Corrige ERROR #10] Usa el nombre completo, igual que el menu."""
    return NOMBRES.get(clave, clave.replace("_", " "))


def pedir_pueblo(texto):
    """Pide un numero de pueblo hasta que sea valido."""
    while True:
        try:
            opcion = int(input(f"Seleccione pueblo de {texto} (1-{len(ORDEN)}): "))
            # [Corrige ERROR #5] Rango inclusivo: 1 y 7 tambien son validos.
            if 1 <= opcion <= len(ORDEN):
                return ORDEN[opcion - 1]
        except ValueError:
            pass
        print("  Opcion invalida, intente de nuevo.")


def listar_pueblos():
    print("Pueblos Magicos disponibles:")
    for i, clave in enumerate(ORDEN, start=1):
        print(f"  {i}. {NOMBRES[clave]}")
    print()


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
    if len(camino) == 1:
        print("  El origen y el destino son el mismo pueblo.")
    else:
        ancho = max(len(mostrar_nombre(p)) for p in camino)
        for a, b in zip(camino, camino[1:]):
            # [Corrige ERROR #6] Peso exacto del tramo a -> b.
            peso = grafo[a][b]
            print(f"  {mostrar_nombre(a):<{ancho}} --({peso:>3} km)--> {mostrar_nombre(b)}")
    print()
    print("  Ruta completa:")
    print("  " + " -> ".join(mostrar_nombre(p) for p in camino))
    print()
    print(f"  Distancia total: {total} km  ({len(camino) - 1} tramo(s))")
    print(LINEA)


def opcion_ruta(grafo):
    """Opcion 1: ruta mas corta entre dos pueblos."""
    listar_pueblos()
    origen = pedir_pueblo("ORIGEN")
    print(f"  -> Origen: {NOMBRES[origen]}")
    destino = pedir_pueblo("DESTINO")
    print(f"  -> Destino: {NOMBRES[destino]}")
    print()
    print("Algoritmo utilizado: Dijkstra")
    camino, total = ruta_mas_corta(grafo, origen, destino)
    imprimir_resultado(grafo, camino, total)


def opcion_conexiones(grafo):
    """Opcion 2: muestra la lista de adyacencia del grafo."""
    print()
    print(LINEA)
    print("  CONEXIONES DIRECTAS (lista de adyacencia)")
    print(LINEA)
    total_aristas = sum(len(v) for v in grafo.values()) // 2
    for clave in ORDEN:
        vecinos = ", ".join(
            f"{mostrar_nombre(v)} ({km} km)"
            for v, km in sorted(grafo[clave].items(), key=lambda x: x[1])
        )
        print(f"  {mostrar_nombre(clave)}:")
        print(f"      {vecinos or '(sin conexiones)'}")
    print()
    print(f"  Vertices: {len(grafo)}   Aristas: {total_aristas}")
    print(LINEA)


def opcion_tabla(grafo):
    """Opcion 3: distancias minimas desde un pueblo hacia todos los demas."""
    listar_pueblos()
    origen = pedir_pueblo("ORIGEN")
    distancias, previo = dijkstra_completo(grafo, origen)

    print()
    print(LINEA)
    print(f"  DISTANCIAS MINIMAS DESDE {mostrar_nombre(origen).upper()}")
    print(LINEA)
    ancho = max(len(mostrar_nombre(p)) for p in ORDEN)
    for destino in sorted(ORDEN, key=lambda p: distancias[p]):
        if destino == origen:
            continue
        if distancias[destino] == INFINITO:
            print(f"  {mostrar_nombre(destino):<{ancho}}   sin ruta")
            continue
        anterior = mostrar_nombre(previo[destino])
        print(f"  {mostrar_nombre(destino):<{ancho}}  {distancias[destino]:>4} km"
              f"   (llega desde {anterior})")
    print(LINEA)


def main():
    grafo = cargar_grafo(leer_datos())

    print(LINEA)
    print("         RUTA MAGICA -- PUEBLA")
    print("   Camino mas corto entre Pueblos Magicos")
    print(LINEA)

    opciones = {
        "1": ("Calcular ruta mas corta entre dos pueblos", opcion_ruta),
        "2": ("Ver conexiones del grafo", opcion_conexiones),
        "3": ("Distancias minimas desde un pueblo", opcion_tabla),
    }

    while True:
        print()
        for num, (texto, _) in opciones.items():
            print(f"  {num}. {texto}")
        print("  0. Salir")
        eleccion = input("Elija una opcion: ").strip()
        print()

        if eleccion == "0":
            print("Gracias por usar Ruta Magica.")
            break
        if eleccion in opciones:
            opciones[eleccion][1](grafo)
        else:
            print("  Opcion invalida, intente de nuevo.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # [Corrige ERROR #11] Salida limpia con Ctrl+C o fin de entrada.
        print("\nPrograma terminado por el usuario.")
    except FileNotFoundError:
        print(f"No se encontro el archivo de datos: {ARCHIVO_DATOS}")
