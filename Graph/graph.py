from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex in self.graph:
            return False

        self.graph[vertex] = []
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            return False

        del self.graph[vertex]

        for neighbors in self.graph.values():
            if vertex in neighbors:
                neighbors.remove(vertex)

        return True

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)

        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)

        if not self.directed:
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)

        return True

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            return False

        if vertex2 not in self.graph[vertex1]:
            return False

        self.graph[vertex1].remove(vertex2)

        if not self.directed:
            if vertex1 in self.graph.get(vertex2, []):
                self.graph[vertex2].remove(vertex1)

        return True

    def has_vertex(self, vertex):
        return vertex in self.graph

    def has_edge(self, vertex1, vertex2):
        return (
            vertex1 in self.graph
            and vertex2 in self.graph[vertex1]
        )

    def get_vertices(self):
        return list(self.graph.keys())

    def get_neighbors(self, vertex):
        if vertex not in self.graph:
            return []

        return self.graph[vertex].copy()

    def degree(self, vertex):
        if vertex not in self.graph:
            return 0

        if self.directed:
            return len(self.graph[vertex])

        return len(self.graph[vertex])

    def bfs(self, start):
        if start not in self.graph:
            return []

        visited = set()
        queue = deque([start])
        result = []

        visited.add(start)

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        if start not in self.graph:
            return []

        visited = set()
        result = []

        def traverse(vertex):
            visited.add(vertex)
            result.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    traverse(neighbor)

        traverse(start)

        return result

    def bfs_path(self, start, target):
        if start not in self.graph or target not in self.graph:
            return []

        queue = deque([start])
        visited = {start}
        previous = {start: None}

        while queue:
            current = queue.popleft()

            if current == target:
                break

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    previous[neighbor] = current
                    queue.append(neighbor)

        if target not in visited:
            return []

        path = []
        current = target

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()
        return path

    def display(self):
        if self.is_empty():
            print("Graph is empty.")
            return

        print("\nGraph (Adjacency List):")

        for vertex, neighbors in self.graph.items():
            if neighbors:
                print(
                    f"{vertex} -> "
                    + " -> ".join(map(str, neighbors))
                )
            else:
                print(f"{vertex} -> []")

    def display_vertices(self):
        if self.is_empty():
            print("Graph is empty.")
            return

        print("Vertices:")
        for vertex in self.graph:
            print(vertex)

    def clear(self):
        self.graph.clear()

    def is_empty(self):
        return len(self.graph) == 0

    def vertex_count(self):
        return len(self.graph)

    def edge_count(self):
        count = sum(
            len(neighbors)
            for neighbors in self.graph.values()
        )

        if self.directed:
            return count

        return count // 2

    def is_connected(self):
        if self.is_empty():
            return True

        start = next(iter(self.graph))
        visited = self.bfs(start)

        return len(visited) == len(self.graph)

    def __len__(self):
        return self.vertex_count()
