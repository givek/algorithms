class Graph:
    def __init__(self):
        self.adj = dict()

    def add_vertex(self, v):
        self.adj[v] = self.adj.get(v, [])

    def remove_vertex(self, v):
        if v in self.adj:
            del self.adj[v]

            for edges in self.adj.values():
                if v in edges:
                    edges.remove(v)

    def add_edge(self, from_v, to_v):
        if from_v in self.adj:
            self.adj[from_v].append(to_v)
        else:
            self.adj[from_v] = [to_v]

    def remove_edge(self, from_v, to_v):
        if from_v in self.adj:
            if to_v in self.adj[from_v]:
                self.adj[from_v].remove(to_v)

    def display(self):
        for k, v in self.adj.items():
            print(f"{k} -> {v}")
        print()


def main():
    g = Graph()

    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")

    g.display()

    g.add_edge("a", "c")
    g.add_edge("b", "a")
    g.add_edge("b", "c")
    g.add_edge("c", "b")

    g.display()

    g.remove_edge("b", "c")

    g.display()

    g.remove_vertex("a")

    g.display()


if __name__ == "__main__":
    main()
