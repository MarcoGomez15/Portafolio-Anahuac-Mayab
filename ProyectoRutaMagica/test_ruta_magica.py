"""
Pruebas de Ruta Magica.

Equipo: Marco Antonio Gomez Fuentes (581874), Amir Moises Hernandez Farah
(584687), Emiliano Peniche Correa (581158), Rodrigo Quijano Lopez (582035).

Cada prueba verifica uno de los errores corregidos de la version 1 o un
requisito del enunciado.
Ejecutar con:   python test_ruta_magica.py
(tambien funcionan con pytest:  pytest test_ruta_magica.py)
"""

import builtins
import contextlib
import io

import ruta_magica as rm

GRAFO = rm.cargar_grafo(rm.leer_datos())

INF = None  # sin conexion directa

# Matriz de adyacencia de referencia del enunciado (km).
# Orden: ZAC, CHI, TET, CUE, TLA, XIC, PAH
MATRIZ_REFERENCIA = [
    [0,   22,  48,  INF, INF, 55,  60],
    [22,  0,   42,  INF, 90,  INF, INF],
    [48,  42,  0,   68,  INF, INF, INF],
    [INF, INF, 68,  0,   38,  115, INF],
    [INF, 90,  INF, 38,  0,   INF, INF],
    [55,  INF, INF, 115, INF, 0,   32],
    [60,  INF, INF, INF, INF, 32,  0],
]


def test_grafo_conserva_todas_las_aristas():
    """ERROR #1: antes Zacatlan solo tenia 1 vecino; debe tener 4."""
    assert set(GRAFO["Zacatlan"]) == {
        "Chignahuapan", "Tetela_de_Ocampo", "Xicotepec", "Pahuatlan"
    }
    total_aristas = sum(len(v) for v in GRAFO.values()) // 2
    assert total_aristas == 10


def test_grafo_no_dirigido():
    """ERROR #2: cada arista debe existir en ambos sentidos con el mismo peso."""
    for a, vecinos in GRAFO.items():
        for b, km in vecinos.items():
            assert GRAFO[b][a] == km
    assert GRAFO["Tlatlauquitepec"]  # antes no tenia salidas


def test_grafo_coincide_con_matriz_de_referencia():
    """Enunciado: el grafo cargado debe ser igual a la matriz de referencia."""
    for i, a in enumerate(rm.ORDEN):
        for j, b in enumerate(rm.ORDEN):
            esperado = MATRIZ_REFERENCIA[i][j]
            if i == j:
                assert esperado == 0
            elif esperado is INF:
                assert b not in GRAFO[a], f"{a}-{b} no deberia estar conectado"
            else:
                assert GRAFO[a].get(b) == esperado, f"{a}-{b} deberia ser {esperado} km"


def test_dijkstra_minimiza_km_no_tramos():
    """ERROR #3: un BFS elegiria el tramo directo de 100 km (1 tramo);
    Dijkstra debe elegir la ruta de 30 km aunque tenga 3 tramos."""
    grafo = rm.cargar_grafo(
        "Zacatlan Cuetzalan 100\n"
        "Zacatlan Chignahuapan 10\n"
        "Chignahuapan Tetela_de_Ocampo 10\n"
        "Tetela_de_Ocampo Cuetzalan 10"
    )
    camino, total = rm.ruta_mas_corta(grafo, "Zacatlan", "Cuetzalan")
    assert total == 30
    assert camino == ["Zacatlan", "Chignahuapan", "Tetela_de_Ocampo", "Cuetzalan"]

    # En el grafo real, el BFS de la v1 daba 170 km (por Xicotepec).
    camino, total = rm.ruta_mas_corta(GRAFO, "Zacatlan", "Cuetzalan")
    assert total == 116
    assert camino == ["Zacatlan", "Tetela_de_Ocampo", "Cuetzalan"]


def test_caminos_no_se_mezclan():
    """ERROR #4: el camino calculado debe coincidir con la suma de sus tramos."""
    for origen in rm.ORDEN:
        for destino in rm.ORDEN:
            camino, total = rm.ruta_mas_corta(GRAFO, origen, destino)
            assert camino[0] == origen and camino[-1] == destino
            assert len(camino) == len(set(camino))  # sin pueblos repetidos
            suma = sum(GRAFO[a][b] for a, b in zip(camino, camino[1:]))
            assert suma == total


def test_menu_acepta_primera_y_ultima_opcion():
    """ERROR #5: las opciones 1 y 7 deben ser validas."""
    original = builtins.input
    try:
        builtins.input = lambda _="": "1"
        assert rm.pedir_pueblo("ORIGEN") == rm.ORDEN[0]
        builtins.input = lambda _="": str(len(rm.ORDEN))
        assert rm.pedir_pueblo("DESTINO") == rm.ORDEN[-1]
    finally:
        builtins.input = original


def test_ejemplos_del_enunciado():
    """Enunciado: Xicotepec -> Tlatlauquitepec = 153 km y
    Pahuatlan -> Tlatlauquitepec = 172 km.
    ERROR #6: cada tramo debe imprimir su propio peso."""
    camino, total = rm.ruta_mas_corta(GRAFO, "Xicotepec", "Tlatlauquitepec")
    assert total == 153
    assert camino == ["Xicotepec", "Cuetzalan", "Tlatlauquitepec"]

    salida = io.StringIO()
    with contextlib.redirect_stdout(salida):
        rm.imprimir_resultado(GRAFO, camino, total)
    texto = salida.getvalue()
    assert "Xicotepec --(115 km)--> Cuetzalan" in texto
    assert "Cuetzalan --( 38 km)--> Tlatlauquitepec" in texto
    assert "Xicotepec -> Cuetzalan -> Tlatlauquitepec" in texto
    assert "Distancia total: 153 km" in texto

    camino, total = rm.ruta_mas_corta(GRAFO, "Pahuatlan", "Tlatlauquitepec")
    assert total == 172
    assert camino == ["Pahuatlan", "Zacatlan", "Chignahuapan", "Tlatlauquitepec"]


def test_sin_ruta_devuelve_none():
    """ERROR #8: sin ruta -> ([], None), no distancia 0."""
    grafo = rm.cargar_grafo("Zacatlan Chignahuapan 22")
    assert rm.ruta_mas_corta(grafo, "Zacatlan", "Cuetzalan") == ([], None)


def test_mismo_origen_y_destino():
    assert rm.ruta_mas_corta(GRAFO, "Cuetzalan", "Cuetzalan") == (["Cuetzalan"], 0)


def test_valida_lineas_mal_formadas():
    """ERROR #9: lineas incompletas o pesos invalidos deben dar error claro."""
    for malo in ("Zacatlan Chignahuapan", "Zacatlan Chignahuapan -5",
                 "Zacatlan Chignahuapan veinte"):
        try:
            rm.cargar_grafo(malo)
        except ValueError:
            continue
        raise AssertionError(f"No se detecto la linea invalida: {malo!r}")


if __name__ == "__main__":
    pruebas = [f for nombre, f in sorted(globals().items())
               if nombre.startswith("test_") and callable(f)]
    for prueba in pruebas:
        prueba()
        print(f"  [OK] {prueba.__name__}")
    print(f"\n{len(pruebas)} pruebas pasaron.")
