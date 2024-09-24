from __future__ import annotations


class Vertex:
    def __init__(self, key: int) -> None:
        self.key = key
        self.neighbors_to_weights: dict[Vertex, int] = {}

    def add_neighbor(self, neighbor: Vertex, weight: int = 0) -> None:
        self.neighbors_to_weights[neighbor] = weight

    def __str__(self):
        return f'{self.key} connected to {[neighbor.key for neighbor in self.neighbors_to_weights]}'

    @property
    def neighbors(self) -> tuple[Vertex, ...]:
        return tuple(self.neighbors_to_weights.keys())


class Graph:
    def __init__(self) -> None:
        self.keys_to_vertices: dict[int, Vertex] = {}

    def add_vertex(self, key: int) -> None:
        self.keys_to_vertices[key] = Vertex(key)

    def get_vertex(self, key: int) -> Vertex | None:
        return self.keys_to_vertices.get(key)

    def __contains__(self, key: int) -> bool:
        return key in self.keys_to_vertices

    def add_edge(self, from_key: int, to_key: int, weight: int = 0) -> None:
        if from_key not in self.keys_to_vertices:
            self.add_vertex(from_key)
        if to_key not in self.keys_to_vertices:
            self.add_vertex(to_key)
        self.keys_to_vertices[from_key].add_neighbor(self.keys_to_vertices[to_key], weight)

    @property
    def vertices(self) -> tuple[int, ...]:
        return tuple(self.keys_to_vertices.keys())

    def __iter__(self):
        return iter(self.keys_to_vertices.values())

    def __str__(self):
        result = f'Directed Graph with vertices: {self.vertices}\n'
        for vertex in self:
            for neighbor, weight in vertex.neighbors_to_weights.items():
                result += f'Edge V{vertex.key} -> V{neighbor.key}, weight {weight}\n'

        return result


if __name__ == "__main__":
    graph = Graph()
    for i in range(6):
        graph.add_vertex(i)

    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 5, 2)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 9)
    graph.add_edge(3, 4, 7)
    graph.add_edge(3, 5, 3)
    graph.add_edge(4, 0, 1)
    graph.add_edge(5, 4, 8)
    graph.add_edge(5, 2, 1)
    print(graph)
