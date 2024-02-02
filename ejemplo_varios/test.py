from collections import deque

def bfs(grafico, inicio, objetivo):
    # Utilizamos una cola para la búsqueda en amplitud
    cola = deque([(inicio, [inicio])])

    while cola:
        nodo, camino = cola.popleft()

        if nodo == objetivo:
            return camino

        for vecino in grafico[nodo]:
            if vecino not in camino:
                cola.append((vecino, camino + [vecino]))

    # Si no se encuentra el objetivo
    return None

# Ejemplo de un grafo representado como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

#Inicio
inicio = 'A'
#Objetivo
objetivo = 'H'

resultado = bfs(grafo, inicio, objetivo)

if resultado:
    print(f"Camino de {inicio} a {objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo}")


