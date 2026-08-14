import heapq


def dijkstra(graph, start):
    if start not in graph.graph:
        return {}

    distances = {vertex: float("inf") for vertex in graph.graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph.graph[current_vertex]:
            if isinstance(neighbor, tuple):
                next_vertex, weight = neighbor
            else:
                next_vertex, weight = neighbor, 1

            distance = current_distance + weight

            if distance < distances[next_vertex]:
                distances[next_vertex] = distance
                heapq.heappush(priority_queue, (distance, next_vertex))

    return distances
