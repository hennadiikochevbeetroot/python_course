from b_graph_adjacency_matrix import Graph

graph = Graph()
for key in range(1, 11):
    graph.set_vertex(key)

graph.add_edge(1, 8)
graph.add_edge(1, 5)
graph.add_edge(1, 2)
graph.add_edge(2, 9)
graph.add_edge(8, 6)
graph.add_edge(8, 4)
graph.add_edge(8, 3)
graph.add_edge(6, 10)
graph.add_edge(6, 7)

# graph.breadth_first_search(graph.get_vertex(1))
graph.depth_first_search(graph.get_vertex(1))
