"""
Ruta Magica -- Proyecto de grafos
"""

import heapq

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
        a, b, peso = partes[0], partes[1], int(partes[2])
        grafo[a] = [(b, peso)]
    return grafo


def dijkstra(grafo, origen, destino):
    """Devuelve (camino, distancia_total) del origen al destino."""
    cola = [origen]
    visitados = {origen}
    distancias = {origen: 0}
    caminos = {origen: [origen]}

    while cola:
        nodo = cola.pop(0)
        if nodo == destino:
            break
        for vecino, peso in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                distancias[vecino] = distancias[nodo] + peso
                caminos[vecino] = caminos[nodo]
                caminos[vecino].append(vecino)
                cola.append(vecino)

    return caminos.get(destino, []), distancias.get(destino, 0)


def mostrar_nombre(clave):
    return clave.replace("_", " ")


def pedir_pueblo(texto):
    while True:
        try:
            opcion = int(input(f"Seleccione pueblo de {texto} (1-{len(ORDEN)}): "))
            if 1 < opcion < len(ORDEN):
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
    main()
