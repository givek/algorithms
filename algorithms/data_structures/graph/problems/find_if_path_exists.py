# Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
# Time: O(N)
# Space: O(N)


def dfs(graph: dict[int, int], visited: set[int], src: int, dest: int):
    if dest in visited:
        return True

    if src in visited:
        return False

    visited.add(src)

    for u in graph[src]:

        is_path = dfs(graph, visited, u, dest)

        if is_path:
            return True

    return False


def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True

    graph = dict()

    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return dfs(graph, set(), source, destination)
