# Ruta Mágica — Puebla

Programa de consola en Python que calcula la **ruta más corta entre Pueblos Mágicos de Puebla** usando el **algoritmo de Dijkstra** sobre un grafo ponderado.

**Autor:** Marco Antonio Gómez Fuentes · **Matrícula:** 581874

## Modelo del problema

| Elemento del grafo | Representa |
|--------------------|------------|
| Vértices (7) | Pueblos Mágicos |
| Aristas (10) | Carreteras entre pueblos (doble sentido → grafo **no dirigido**) |
| Pesos | Distancia en kilómetros |

```
            Pahuatlan
           /32       \60
   Xicotepec ---55--- Zacatlan ---22--- Chignahuapan
        |               |48      42 /         |
        |115         Tetela de Ocampo         |90
        |               |68                   |
        +---------- Cuetzalan ---38--- Tlatlauquitepec
```

Las conexiones están en `pueblos.txt`, una por línea: `PuebloA PuebloB km`.

## Cómo funciona Dijkstra aquí

1. Todas las distancias empiezan en ∞, excepto la del origen, que es 0.
2. Una cola de prioridad (`heapq`) entrega siempre el pueblo con la menor distancia acumulada.
3. Para cada vecino se prueba si pasar por el pueblo actual acorta el camino (*relajación*). Si es así, se actualiza su distancia y su predecesor.
4. Al terminar, el camino se reconstruye siguiendo los predecesores desde el destino.

Complejidad: **O((V + E) log V)**.

## Uso

Requiere Python 3.8 o superior. No usa librerías externas.

```bash
python ruta_magica.py        # ejecutar el programa
python test_ruta_magica.py   # correr las pruebas
```

Opciones del menú:

1. **Calcular ruta más corta** entre dos pueblos, con el detalle de cada tramo.
2. **Ver conexiones del grafo** (lista de adyacencia).
3. **Distancias mínimas desde un pueblo** hacia todos los demás.

Ejemplo:

```
  Zacatlan de las Manzanas --( 48 km)--> Tetela de Ocampo
  Tetela de Ocampo         --( 68 km)--> Cuetzalan del Progreso

  Distancia total: 116 km  (2 tramo(s))
```

## Estructura

```
ruta-magica/
├── ruta_magica.py                  # Programa (versión 2, entregable)
├── pueblos.txt                     # Datos del grafo
├── test_ruta_magica.py             # Pruebas automáticas
├── CAMBIOS.md                      # Errores de la v1 y cómo se corrigieron
└── versiones/
    └── ruta_magica_v1_original.py  # Versión original con los errores comentados
```

## Historial

La versión 1 tenía 11 errores. El más grave: no implementaba Dijkstra (era una búsqueda en anchura) y el grafo perdía conexiones al cargarse. Por eso, de Zacatlán a Cuetzalan respondía 170 km en lugar de 116 km. Todos los errores y sus correcciones están documentados en [CAMBIOS.md](CAMBIOS.md).
