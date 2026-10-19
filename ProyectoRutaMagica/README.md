# Ruta Mágica — Puebla

Programa de consola en Python que calcula la **ruta más corta entre Pueblos Mágicos de Puebla** usando el **algoritmo de Dijkstra** sobre un grafo ponderado.

## Equipo

| Integrante | Matrícula |
|------------|-----------|
| Marco Antonio Gómez Fuentes | 581874 |
| Amir Moisés Hernández Farah | 584687 |
| Emiliano Peniche Correa | 581158 |
| Rodrigo Quijano López | 582035 |

## Modelo del problema

| Elemento del grafo | Representa |
|--------------------|------------|
| Vértices (7) | Pueblos Mágicos de la Sierra Norte de Puebla |
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

**Representación:** lista de adyacencia (diccionario de diccionarios), la recomendada para grafos dispersos: hay 10 de las 21 aristas posibles. Las conexiones están en `pueblos.txt`, una por línea: `PuebloA PuebloB km`.

## Justificación del algoritmo

| Algoritmo | ¿Por qué sí o por qué no? |
|-----------|---------------------------|
| **Dijkstra** ✔ | Todas las distancias son positivas y cada consulta va de **un** origen a **un** destino. Con cola de prioridad es **O((V + E) log V)**, el más eficiente de los tres. |
| Floyd-Warshall | Calcula todos los pares con una matriz V×V, O(V³). Es trabajo de más para una sola consulta. |
| Bellman-Ford | Solo se necesita con pesos negativos, que en kilómetros no existen. Es más lento: O(V·E). |

## Cómo funciona Dijkstra aquí

1. Todas las distancias empiezan en ∞, excepto la del origen, que es 0.
2. Una cola de prioridad (`heapq`) entrega siempre el pueblo con la menor distancia acumulada.
3. Para cada vecino se prueba si pasar por el pueblo actual acorta el camino (*relajación*). Si es así, se actualiza su distancia y su predecesor.
4. Al terminar, el camino se reconstruye siguiendo los predecesores desde el destino.

## Uso

Requiere Python 3.8 o superior. No usa librerías externas.

```bash
python ruta_magica.py        # ejecutar el programa
python test_ruta_magica.py   # correr las 10 pruebas
```

Ejemplo (igual a la "Ejecución Esperada" del enunciado):

```
 Seleccione pueblo de ORIGEN (1-7): 6
   -> Origen: Xicotepec de Juarez

 Seleccione pueblo de DESTINO (1-7): 5
   -> Destino: Tlatlauquitepec

 Algoritmo utilizado: Dijkstra
 Calculando ruta mas corta...

================================================================
   [OK] RUTA ENCONTRADA
================================================================

   Xicotepec --(115 km)--> Cuetzalan
   Cuetzalan --( 38 km)--> Tlatlauquitepec

   Ruta completa:
   Xicotepec -> Cuetzalan -> Tlatlauquitepec

   Distancia total: 153 km
================================================================
```

## Estructura

```
ProyectoRutaMagica/
├── ruta_magica.py                  # Programa (versión 2, entregable)
├── pueblos.txt                     # Datos del grafo
├── test_ruta_magica.py             # Pruebas automáticas
├── CAMBIOS.md                      # Errores de la v1 y cómo se corrigieron
└── versiones/
    └── ruta_magica_v1_original.py  # Versión original con los errores comentados
```

## Historial

La versión 1 tenía 10 errores. El más grave: no implementaba Dijkstra (era una búsqueda en anchura) y el grafo perdía conexiones al cargarse. Por eso, de Zacatlán a Cuetzalan respondía 170 km en lugar de 116 km. Todos los errores y sus correcciones están en [CAMBIOS.md](CAMBIOS.md).
