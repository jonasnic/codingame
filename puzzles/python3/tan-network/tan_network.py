import math
from collections import defaultdict
from typing import Dict, List, Optional, Set


class Node:
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.routes: List[str] = []


class Graph:
    def __init__(self, nodes: Dict[str, Node], start_id: str, end_id: str):
        self.nodes: Dict[str, Node] = nodes
        self.start_id = start_id
        self.end_id = end_id

    @property
    def start_node(self) -> Node:
        return self.nodes[self.start_id]

    @property
    def end_node(self) -> Node:
        return self.nodes[self.end_id]


def distance(node1: Node, node2: Node) -> float:
    EARTH_RADIUS = 6371
    x = (node2.longitude - node1.longitude) * math.cos((node1.latitude + node2.latitude) / 2)
    y = node2.latitude - node1.latitude
    return math.hypot(x, y) * EARTH_RADIUS


def read_game_input() -> Graph:
    nodes: Dict[str, Node] = {}
    start_id = input()
    end_id = input()

    n = int(input())
    for i in range(n):
        stop: List[str] = input().split(',')
        identifier = stop[0]
        name = stop[1].replace('\"', '')
        latitude = math.radians(float(stop[3]))
        longitude = math.radians(float(stop[4]))
        node = Node(name, latitude, longitude)
        nodes[identifier] = node

    m = int(input())
    for i in range(m):
        idA, idB = input().split(' ')
        nodes[idA].routes.append(idB)

    return Graph(nodes, start_id, end_id)


def traverse_with_a_star(graph: Graph) -> Optional[Dict[str, str]]:
    """Compute the shortest path between start_id and end_id with the A* search algorithm."""
    # initialization
    closed_set: Set[str] = set()  # set of node ids already evaluated
    open_set: Set[str] = {graph.start_id}  # set of node ids to evaluate
    came_from: Dict[str, str] = {}  # node_id => parent node id on the shortest path
    g_scores: Dict[str, float] = defaultdict(lambda: math.inf)  # node_id => cost from start_node
    f_scores: Dict[str, float] = defaultdict(lambda: math.inf)  # node_id => g_score + h_cost to end_node
    g_scores[graph.start_id] = 0.0
    f_scores[graph.start_id] = distance(graph.start_node, graph.end_node)

    # loop until end_node is found or we run out of nodes to evaluate
    while open_set:
        current_id: Optional[str] = compute_minimum(open_set, f_scores)
        if not current_id:
            return None
        if current_id == graph.end_id:
            return came_from
        # mark current as visited
        open_set.remove(current_id)
        closed_set.add(current_id)

        # explore neighbors
        for neighbor_id in graph.nodes[current_id].routes:
            if neighbor_id in closed_set:
                continue  # already evalutated this node
            neighbor_node = graph.nodes[neighbor_id]
            g_score = g_scores[current_id] + distance(graph.nodes[current_id], neighbor_node)
            if neighbor_id not in open_set:
                open_set.add(neighbor_id)  # first time we explore this node id
            elif g_score >= g_scores[neighbor_id]:
                continue  # we already explored this node and the new cost is more expensive
            came_from[neighbor_id] = current_id
            g_scores[neighbor_id] = g_score
            f_scores[neighbor_id] = g_score + distance(neighbor_node, graph.end_node)
    return None


def compute_minimum(open_set, f_scores) -> Optional[str]:
    """Compute the node_id in open_set with the minimum f_score"""
    min_id: Optional[str] = None
    min_f_score = math.inf
    for identifier in open_set:
        f_score = f_scores[identifier]
        if f_score < min_f_score:
            min_id = identifier
            min_f_score = f_score
    return min_id


def reconstruct_path(graph: Graph, came_from: Dict[str, str]) -> List[str]:
    current_id = graph.end_id
    stack: List[str] = []

    while current_id in came_from:
        stack.append(current_id)
        current_id = came_from[current_id]
    stack.append(current_id)
    return stack


def print_solution(graph: Graph, came_from: Optional[Dict[str, str]]):
    if came_from is None:
        print("IMPOSSIBLE")
    else:
        path: List[str] = reconstruct_path(graph, came_from)
        while path:
            node = graph.nodes[path.pop()]
            print(node.name)


if __name__ == "__main__":
    graph = read_game_input()
    came_from: Optional[Dict[str, str]] = traverse_with_a_star(graph)
    print_solution(graph, came_from)
