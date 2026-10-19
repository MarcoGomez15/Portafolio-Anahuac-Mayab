# Registro de cambios — Ruta Mágica

**Equipo:** Marco Antonio Gómez Fuentes (581874) · Amir Moisés Hernández Farah (584687) · Emiliano Peniche Correa (581158) · Rodrigo Quijano López (582035)

## Versión 2.0 (corregida)

Revisión de la versión 1 (`versiones/ruta_magica_v1_original.py`) contra el enunciado "Ruta mágica — Proyecto de grafos". En ese archivo, cada error está marcado en el código con `ERROR #n`. En `ruta_magica.py`, la corrección correspondiente está marcada con `[Corrige ERROR #n]`.

**Ejemplo del impacto:** de Zacatlán a Cuetzalan, la v1 respondía **170 km** (por Xicotepec). La ruta más corta real es **116 km** (por Tetela de Ocampo).

### Errores críticos (el programa daba resultados incorrectos)

| # | Función | Error en v1 | Corrección en v2 |
|---|---------|-------------|------------------|
| 1 | `cargar_grafo` | `grafo[a] = [(b, peso)]` reemplazaba la lista en cada línea. Cada pueblo conservaba solo su última conexión. | Se agrega cada vecino a un diccionario: `grafo[a][b] = peso`. |
| 2 | `cargar_grafo` | Las aristas solo se guardaban en un sentido (a → b). Tlatlauquitepec quedaba sin salidas. | Grafo no dirigido, como pide el enunciado: se guarda `a → b` y `b → a`. |
| 3 | `dijkstra` | No era Dijkstra, era una búsqueda en anchura (BFS): cola FIFO y nodos marcados al descubrirlos. Minimizaba el número de tramos, no los kilómetros. | Dijkstra con cola de prioridad (`heapq`) y relajación de aristas. |
| 4 | `dijkstra` | `caminos[vecino] = caminos[nodo]` no copiaba la lista. Varios caminos compartían la misma y se mezclaban. | Se guarda el predecesor de cada pueblo y el camino se reconstruye al final (`reconstruir_camino`). |
| 5 | `pedir_pueblo` | `1 < opcion < len(ORDEN)` rechazaba las opciones 1 y 7. | Rango inclusivo: `1 <= opcion <= len(ORDEN)`. |
| 6 | `imprimir_resultado` | `grafo[a][0][1]` mostraba el peso del primer vecino, no el del tramo a → b. | `grafo[a][b]`. |

### Errores menores

| # | Error en v1 | Corrección en v2 |
|---|-------------|------------------|
| 7 | `heapq` se importaba pero no se usaba. | Ahora es la base de la cola de prioridad. |
| 8 | Sin ruta devolvía distancia `0`, lo mismo que origen = destino. | Devuelve `([], None)`. |
| 9 | No se validaba el formato de los datos. | Error claro si una línea no tiene 3 partes o la distancia no es un entero ≥ 0. |
| 10 | Ctrl+C mostraba un traceback. | Salida limpia con un mensaje. |

> Los nombres cortos en la ruta ("Zacatlan", "Tetela de Ocampo") **no son un error**: el enunciado los usa así en la "Ejecución Esperada".

### Ajustes para cumplir el enunciado

- **Justificación del algoritmo** (en el encabezado de `ruta_magica.py` y en el README): se eligió Dijkstra porque todas las distancias son positivas y cada consulta va de un origen a un destino.
- **Formato de salida** igual a la "Ejecución Esperada": lista de pueblos al inicio, "Algoritmo utilizado: Dijkstra" solo en la primera consulta, tramos con nombres cortos y pregunta "¿Desea consultar otra ruta? (S/N)".
- Los datos se leen desde `pueblos.txt`, con el formato de archivo del enunciado.
- Pruebas automáticas en `test_ruta_magica.py` (10): una por cada error corregido, los dos ejemplos del enunciado (153 km y 172 km) y una comparación del grafo con la matriz de adyacencia de referencia.
