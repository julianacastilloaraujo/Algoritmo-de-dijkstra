# Desarrollado por Brayan Baquero y Juliana Castillo
# Asignatura de Inteligencia Artificial 
# Profesor : Manuel Alexander Cadena 
# Universidad de Cundinamarca
# Ingenieria de Sistemas

import sys
def dijkstra_con_direccionalidad(grafo, origen):
    visitados = set()
    distancia = {nodo: sys.maxsize for nodo in grafo}
    distancia[origen] = 0
    ruta_mas_corta = {}
    while len(visitados) != len(grafo):
        nodo_actual = min((nodo for nodo in grafo if nodo not in visitados), key=lambda n: distancia[n])
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia[nodo_actual] + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                ruta_mas_corta[vecino] = nodo_actual
    return distancia, ruta_mas_corta
num_nodos = int(input("Ingrese el número de nodos: "))
grafo = {}
for i in range(num_nodos):
    valor_nodo = input(f"Ingrese el valor para el nodo {i}: ")
    grafo[valor_nodo] = {}
for nodo in grafo:
    num_aristas = int(input(f"Ingrese el número de aristas para el nodo {nodo}: "))
    for i in range(num_aristas):
        vecino = input(f"Ingrese el vecino para el nodo {nodo}: ")
        peso = int(input(f"Ingrese el peso para la arista {nodo} -> {vecino}: "))
        grafo[nodo][vecino] = peso
origen = input("Ingrese el nodo de origen: ")
distancia, ruta_mas_corta = dijkstra_con_direccionalidad(grafo, origen)
print("Distancias más cortas desde el nodo de origen:")
for nodo, dist in distancia.items():
    print(f"Nodo: {nodo}, Distancia: {dist}")
print("Ruta más corta hacia cada nodo:")
for nodo, ruta in ruta_mas_corta.items():
    print(f"Nodo: {nodo}, Ruta: {ruta} -> {nodo}")