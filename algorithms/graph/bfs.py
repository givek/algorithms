# Time: O(V + E)
# Space: O(V)
from algorithms.data_structures.graph.graph import Graph


# Can be used for finding the shortest path between two vertices.

# Time complexity is O(V + 2E) for undirected graphs and O(V + E) for directed graphs.


# def graph_bfs(s, graph):
#     level = {s: 0}
#     parent = {s: None}
#
#     i = 1
#
#     frontier = [s]
#
#     while frontier:
#         next = []
#
#         for u in frontier:
#             for v in graph.associated_vertices(u):
#                 if v not in level:
#                     level[v] = i
#                     parent[v] = u
#                     next.append(v)
#
#         frontier = next
#         i += 1


def bfs(s, graph):
    vertices = [s]
    visited = set()

    while vertices:
        vertex = vertices.pop(0)

        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            vertices.extend(graph.associated_vertices(vertex))


def main():
    g = Graph()

    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")

    g.add_edge("a", "c")
    g.add_edge("b", "a")
    g.add_edge("b", "c")
    g.add_edge("c", "b")

    # graph_bfs("a", g)
    bfs("a", g)


if __name__ == "__main__":
    main()
