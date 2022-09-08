from algorithms.data_structures.graph.graph import Graph


def graph_bfs(s, graph):
    level = {s: 0}
    parent = {s: None}

    i = 1

    frontier = [s]

    while frontier:
        next = []

        for u in frontier:
            for v in graph.associated_vertices(u):
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)

        frontier = next
        i += 1


def main():
    g = Graph()

    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")

    g.add_edge("a", "c")
    g.add_edge("b", "a")
    g.add_edge("b", "c")
    g.add_edge("c", "b")

    graph_bfs("a", g)


if __name__ == "__main__":
    main()
