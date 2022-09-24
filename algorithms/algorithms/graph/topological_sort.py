from algorithms.data_structures.graph.graph import Graph


def dfs_visit(graph: Graph, visited: set, topological_order: list, s):
    visited.add(s)

    for vertex in graph.associated_vertices(s):
        if vertex not in visited:
            dfs_visit(graph, visited, topological_order, vertex)

    topological_order.append(s)


def topological_sort(graph: Graph):
    visited = set()
    topological_order = []

    for s in graph.vertices():
        if s not in visited:
            visited.add(s)
            dfs_visit(graph, visited, topological_order, s)

    return list(reversed(topological_order))


def main():
    g = Graph()

    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)

    g.add_edge(1, 2)
    g.add_edge(1, 5)

    g.add_edge(2, 3)

    # 3 zero out edges

    # 4 zero out edges

    g.add_edge(5, 3)
    g.add_edge(5, 4)

    g.add_edge(6, 1)
    g.add_edge(6, 5)

    # add cycle: 6 -> 1 -> 5 -> 6
    # g.add_edge(5, 6)

    print(topological_sort(g))


if __name__ == "__main__":
    main()
