# Link: https://leetcode.com/problems/find-center-of-star-graph/
# Time: O(N)
# Space: O(N)


def find_center(edges: list[list[int]]) -> int:
    star_graph = dict()

    for u, v in edges:
        # Graph is undirected so, add both u and v.

        if u in star_graph:
            star_graph[u].append(v)
        else:
            star_graph[u] = [v]

        if v in star_graph:
            star_graph[v].append(u)
        else:
            star_graph[v] = [u]

    for u in star_graph:
        # if degree of any vertex in the graph is equal to (n - 1), it the centre node.
        if len(star_graph[u]) == len(star_graph) - 1:
            return u


def main():
    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(find_center(edges))


if __name__ == "__main__":
    main()
