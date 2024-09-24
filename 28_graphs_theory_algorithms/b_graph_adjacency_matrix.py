from __future__ import annotations
import enum
import heapq
import sys


class VertexColor(str, enum.Enum):
    WHITE = 'white'   # Unprocessed vertex
    GRAY = 'gray'     # Neighbor processed vertex
    BLACK = 'black'   # Fully processed vertex


class Vertex:
    def __init__(self, key: int) -> None:
        self.key = key
        self.neighbors_to_weights: dict[Vertex, int] = {}
        self.color = VertexColor.WHITE
        self.distance = sys.maxsize   # float('inf')
        self.previous = None
        self.discovery_time = 0
        self.closing_time = 0

    def __lt__(self, other: Vertex) -> bool:
        return self.key < other.key

    def get_neighbor_weight(self, neighbor: Vertex) -> int:
        return self.neighbors_to_weights.get(neighbor, 0)

    def set_neighbor_weight(self, neighbor: Vertex, weight: int = 0):
        self.neighbors_to_weights[neighbor] = weight

    def get_neighbors(self) -> tuple[Vertex, ...]:
        return tuple(sorted(self.neighbors_to_weights.keys(), key=lambda vertex: vertex.key))

    def __str__(self):
        return "{:^8}|{:^8}|{:^8}|{:^8}|{:^8}| {}".format(
            self.key,
            self.color,
            self.distance,
            self.discovery_time,
            self.closing_time,
            self.previous,
        )


class Graph:
    def __init__(self):
        self.keys_to_vertices: dict[int, Vertex] = {}
        self.edges: dict[tuple[int, int], int] = {}   # (source, destination): weight
        self.time = 0

    def __iter__(self):
        return iter(sorted(self.keys_to_vertices.values(), key=lambda v: v.key))

    def __len__(self):
        return len(self.keys_to_vertices)

    def __contains__(self, key: int) -> bool:
        return key in self.keys_to_vertices

    def get_vertex(self, key: int) -> Vertex:
        return self.keys_to_vertices.get(key)

    def set_vertex(self, key: int) -> None:
        self.keys_to_vertices[key] = Vertex(key)

    def add_edge(self, from_key: int, to_key: int, weight: int = 0):
        if from_key not in self.keys_to_vertices:
            self.set_vertex(from_key)
        if to_key not in self.keys_to_vertices:
            self.set_vertex(to_key)

        self.keys_to_vertices[from_key].set_neighbor_weight(self.keys_to_vertices[to_key], weight)
        self.edges[(from_key, to_key)] = weight

    def print_distances(self):
        print('--------------------------------------------')
        for vertex in self:
            print(f'Distance to vertex {vertex.key} = {vertex.distance}')

    def reset_distances(self, default_distance: int = sys.maxsize):
        for vertex in self:
            vertex.distance = default_distance

    # BFS Algorithm (solved with list as Queue)
    # Finds shortest distance from start_vertex to all others
    def breadth_first_search(self, start_vertex: Vertex):
        start_vertex.distance = 0
        start_vertex.previous = None
        vertices_queue = [start_vertex]
        while len(vertices_queue) > 0:
            current_vertex = vertices_queue.pop(0)
            print('Visiting Vertex ', current_vertex.key)
            for neighbor in current_vertex.get_neighbors():
                # WHITE - non-visited neighbor
                if neighbor.color == VertexColor.WHITE:
                    # GRAY - becomes an enqueued neighbor
                    neighbor.color = VertexColor.GRAY
                    neighbor.distance = current_vertex.distance + 1
                    neighbor.previous = current_vertex
                    vertices_queue.append(neighbor)
            # After graying all neighbors, current vertex is blacked - means completely processed
            current_vertex.color = VertexColor.BLACK

    # DFS Algorithm (solved with recursive visiting next neighbors and backtracking)
    def depth_first_search(self, start_vertex: Vertex):
        print('Visiting Vertex ', start_vertex.key)
        start_vertex.color = VertexColor.GRAY
        self.time += 1
        start_vertex.discovery_time = self.time
        for next_vertex in start_vertex.get_neighbors():
            if next_vertex.color == VertexColor.WHITE:
                # If not visited yet (is white), then set it to backtrack and visit it recursively
                next_vertex.previous = start_vertex
                self.depth_first_search(next_vertex)
        # Once finished all recursive visits to neighbors, set current to be blacked, as already processed
        start_vertex.color = VertexColor.BLACK
        self.time += 1
        start_vertex.closing_time = self.time

    # Dijkstra Algorithm (solved with heap as Priority Queue)
    # Finds shortest path between vertices
    def dijkstra(self, start_vertex: Vertex):
        start_vertex.distance = 0
        not_yet_visited: list[list[int | Vertex]] = [[start_vertex.distance, start_vertex]]
        heapq.heapify(not_yet_visited)
        while not_yet_visited:
            current_vertex: Vertex = heapq.heappop(not_yet_visited)[1]
            self.print_distances()
            for next_vertex in current_vertex.get_neighbors():
                new_distance = current_vertex.distance + current_vertex.get_neighbor_weight(next_vertex)
                if new_distance < next_vertex.distance:
                    next_vertex.distance = new_distance
                    next_vertex.previous = current_vertex
                    found = False
                    for distance_vertex in not_yet_visited:
                        if distance_vertex[1].key == next_vertex.key:
                            distance_vertex[0] = next_vertex.distance
                            heapq.heapify(not_yet_visited)
                            found = True
                    if not found:
                        heapq.heappush(not_yet_visited, [next_vertex.distance, next_vertex])

    # Homework - do it autonomously as an extra task

    # Bellman-Ford Algorithm
    def bellman_ford(self, start_vertex: Vertex):
        pass

    # Prim Algorithm
    def prim(self, start_vertex: Vertex):
        pass
