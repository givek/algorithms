# Time: O(V + E)
# Space: O(N)


from algorithms.data_structures.graph.graph import Graph


def dfs(graph):  # visit the entire graph
    visited = set()
    parent = dict()
    for s in graph.vertices():
        if s not in parent:
            parent[s] = None
            visited.add(s)
            dfs_visit(graph, visited, parent, s)
        print()

    print(parent)


def dfs_visit(graph, visited, parent, s):
    print(s)  # pre-order traversal
    # visited.add(s)
    for w in graph.associated_vertices(s):
        if w not in parent:
            parent[w] = s
            dfs_visit(graph, visited, parent, w)
    # print(s)  # post-order traversal


def main():
    g = Graph()

    g.add_vertex("0")
    g.add_vertex("1")
    g.add_vertex("2")
    g.add_vertex("3")
    g.add_vertex("4")

    g.add_vertex("5")
    g.add_vertex("6")
    # g.add_vertex("5")
    # g.add_vertex("6")
    # g.add_vertex("7")
    # g.add_vertex("8")
    # g.add_vertex("9")

    # g.add_edge("5", "6")

    g.add_edge("0", "1")
    g.add_edge("0", "2")
    g.add_edge("0", "3")

    g.add_edge("1", "0")
    g.add_edge("1", "3")

    g.add_edge("2", "0")
    g.add_edge("2", "3")

    g.add_edge("3", "0")
    g.add_edge("3", "1")
    g.add_edge("3", "2")
    g.add_edge("3", "4")

    g.add_edge("4", "3")

    g.display()

    dfs(g)


if __name__ == "__main__":
    main()
