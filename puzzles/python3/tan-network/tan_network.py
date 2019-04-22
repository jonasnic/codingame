import math
from collections import defaultdict


class Node:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat  # latitude
        self.lon = lon  # longitude
        self.routes = []


class Graph:
    def __init__(self, nodes, start_id, end_id):
        self.nodes = nodes  # node id => node object
        self.start_id = start_id
        self.end_id = end_id

    @property
    def start_node(self):
        return self.nodes[self.start_id]

    @property
    def end_node(self):
        return self.nodes[self.end_id]


def distance(nodeA, nodeB):
    EARTH_RADIUS = 6371
    x = (nodeB.lon - nodeA.lon) * math.cos((nodeA.lat + nodeB.lat) / 2)
    y = nodeB.lat - nodeA.lat
    return math.hypot(x, y) * EARTH_RADIUS


def h_cost(nodeA, nodeB):
    return distance(nodeA, nodeB)


def read_game_input():
    nodes = {}
    start_id = input()
    end_id = input()

    n = int(input())
    for i in range(n):
        stop = input().split(',')
        identifier = stop[0]
        name = stop[1].replace('\"', '')
        lat = math.radians(float(stop[3]))
        lon = math.radians(float(stop[4]))
        node = Node(name, lat, lon)
        nodes[identifier] = node

    m = int(input())
    for i in range(m):
        idA, idB = input().split(' ')
        nodes[idA].routes.append(idB)

    return Graph(nodes, start_id, end_id)


def a_star(graph):
    """Compute the shortest path between start_id and end_id with A*"""
    # initialization
    closed_set = set()  # set of node ids already evaluated
    open_set = {graph.start_id}  # set of node ids to evaluate
    came_from = {}  # node_id => parent node id on the shortest path
    g_scores = defaultdict(lambda: math.inf)  # node_id => cost from start_node
    f_scores = defaultdict(lambda: math.inf)  # node_id => g_score + h_cost to end_node
    g_scores[graph.start_id] = 0
    f_scores[graph.start_id] = h_cost(graph.start_node, graph.end_node)

    # loop until end_node is found or we run out of nodes to evaluate
    while len(open_set) != 0:
        current_id = minimum(open_set, f_scores)
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
            f_scores[neighbor_id] = g_score + h_cost(neighbor_node, graph.end_node)
    return None


def minimum(open_set, f_scores):
    """Compute the node_id in open_set with the minimum f_score"""
    min_id = None
    min_f_score = math.inf
    for identifier in open_set:
        f_score = f_scores[identifier]
        if f_score < min_f_score:
            min_id = identifier
            min_f_score = f_score
    return min_id


def reconstruct_path(graph, came_from):
    current_id = graph.end_id
    stack = []

    while current_id in came_from:
        stack.append(current_id)
        current_id = came_from[current_id]
    stack.append(current_id)
    return stack


def print_solution(graph, came_from):
    if came_from is None:
        print("IMPOSSIBLE")
    else:
        path = reconstruct_path(graph, came_from)
        while len(path) != 0:
            node = graph.nodes[path.pop()]
            print(node.name)


graph = read_game_input()
came_from = a_star(graph)
print_solution(graph, came_from)
