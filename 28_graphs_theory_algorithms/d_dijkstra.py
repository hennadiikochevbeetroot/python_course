from b_graph_adjacency_matrix import Graph

graph = Graph()
for key in range(0, 6):
    graph.set_vertex(key)

graph.add_edge(0, 1, 5)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 2, 4)
graph.add_edge(2, 3, 9)
graph.add_edge(3, 4, 7)
graph.add_edge(3, 5, 3)
graph.add_edge(4, 0, 1)
graph.add_edge(5, 2, 1)
graph.add_edge(5, 4, 8)

graph.dijkstra(graph.get_vertex(0))
