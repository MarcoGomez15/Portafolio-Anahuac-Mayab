# Registro de cambios — Ruta Mágica

## Versión 2.0 (corregida)

Revisión de la versión 1 (`versiones/ruta_magica_v1_original.py`). En ese archivo, cada error está marcado en el código con `ERROR #n`. En `ruta_magica.py`, la corrección correspondiente está marcada con `[Corrige ERROR #n]`.

**Ejemplo del impacto:** de Zacatlán a Cuetzalan, la v1 respondía **170 km** (por Xicotepec). La ruta más corta real es **116 km** (por Tetela de Ocampo).

### Errores críticos (el programa daba resultados incorrectos)

| # | Función | Error en v1 | Corrección en v2 |
|---|---------|-------------|------------------|
| 1 | `cargar_grafo` | `grafo[a] = [(b, peso)]` reemplazaba la lista en cada línea. Cada pueblo conservaba solo su última conexión. | Se agrega cada vecino a un diccionario: `grafo[a][b] = peso`. |
| 2 | `cargar_grafo` | Las aristas solo se guardaban en un sentido (a → b). Tlatlauquitepec quedaba sin salidas. | Grafo no dirigido: se guarda `a → b` y `b → a`. |
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
| 10 | La ruta mostraba "Zacatlan" y el menú "Zacatlan de las Manzanas". | Ambos usan el diccionario `NOMBRES`. |
| 11 | Ctrl+C mostraba un traceback. | Salida limpia con un mensaje. |

### Mejoras añadidas

- Los datos se leen desde `pueblos.txt`, así que se pueden agregar pueblos sin tocar el código.
- Menú principal con tres opciones: ruta más corta, ver conexiones (lista de adyacencia) y tabla de distancias mínimas desde un pueblo.
- `dijkstra_completo` calcula las distancias a todos los pueblos y se reutiliza en las opciones 1 y 3.
- Pruebas automáticas en `test_ruta_magica.py`, una por cada error corregido.
