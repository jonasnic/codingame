class Node:
    def __init__(self, node_id):
        self.children = set()
        self.depth = 0


class Graph:
    def __init__(self):
        self.nodes = {}  # node_id => set of children ids

    def build(self): 
        nb_edges = int(input())  # the number of relationships of influence
        for _ in range(nb_edges):
            parent_id, child_id = map(int, input().split())
            parent = None
            child = None

            if child_id in self.nodes:
                child = self.nodes[child_id]
            else:
                child = Node(child_id)
                self.nodes[child_id] = child

            if parent_id in self.nodes:
                parent = self.nodes[parent_id]
                parent.children.add(child_id)
            else:
                parent = Node(parent_id)
                parent.children.add(child_id)
                self.nodes[parent_id] = parent

    def solve(self):
        """Returns the number of people involved in the longest succession of influences."""
        max_depth = 0
        for node in self.nodes.values():
            self.traverse(node)
        for node in self.nodes.values():
            if node.depth > max_depth:
                max_depth = node.depth
        return max_depth + 1

    def traverse(self, node):
        for child_id in node.children:
            child = self.nodes[child_id]
            if child.depth <= node.depth:
                child.depth = node.depth + 1
                self.traverse(child)


if __name__ == "__main__":
    graph = Graph()
    graph.build()
    print(graph.solve())
