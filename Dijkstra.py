def dijkstra(current, nodes, distances):
    unvisited = {node: None for node in nodes}
    visited = {}
    currentDistance = 0
    unvisited[current] = currentDistance
    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [(node, dist) for node, dist in unvisited.items() if dist is not None]
        print(sorted(candidates, key=lambda x: x[1]))
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
    return visited

nodes = ('A', 'B', 'C', 'D', 'E')
distances = {
    'A': {'B': 5, 'C': 2},
    'B': {'C': 2, 'D': 3},
    'C': {'B': 3, 'D': 7},
    'D': {'E': 7},
    'E': {'D': 9}
}
current = 'A'

print(dijkstra(current, nodes, distances))
