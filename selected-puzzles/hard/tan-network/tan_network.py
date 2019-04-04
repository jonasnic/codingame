import math


class Node:
    def __init__(self, identifier, full_name, lat, lon):
        self.routes = []
        self.identifier = identifier
        self.full_name = full_name
        self.lat = lat  # latitude
        self.lon = lon  # longitude

    def distance(self, other):
        x = (other.lon - self.lon) * math.cos((self.lat + other.lat) / 2)
        y = other.lat - self.lat
        return math.hypot(x, y) * 6371


class Graph:
    def __init__(self):
        self.nodes = {}  # identifier, node

    def read_game_input(self):
        self.start_id = input()  # start id
        self.end_id = input()  # end id
        nb_stops = int(input())
        for _ in range(nb_stops):
            line = input().split(",")
            identifier = line[0]
            full_name = line[1].replace("\"", "", 2)
            lat = math.radians(float(line[3]))
            lon = math.radians(float(line[4]))
            node = Node(identifier, full_name, lat, lon)
            self.nodes[identifier] = node

        nb_routes = int(input())
        for _ in range(nb_routes):
            route = input().split(" ")
            identifier1 = route[0]
            identifier2 = route[1]
            self.nodes[identifier1].routes.append(identifier2)

    def search(self):
        """Compute the shortest path between start and end using A*
        Reference: https://en.wikipedia.org/wiki/A*_search_algorithm
        """
        closed = set()  # set of ids already evaluated
        opened = set()  # set of discovered ids that are not evaluated yet
        parents = {}  # identifier: parent_id
        g_scores = {}  # identifier: g_score
        f_scores = {}  # identifier: f_score
        opened.add(self.start_id)
        g_scores[self.start_id] = 0
        f_scores[self.start_id] = self.h_cost(self.nodes[self.start_id])

        while len(opened) != 0:
            min_id = self.minimum(opened, f_scores)
            if min_id is None:
                min_id = opened.pop()
            else:
                opened.remove(min_id)
            if min_id == self.end_id:
                return parents  # search is done
            closed.add(min_id)
            self.explore(
                min_id, closed, opened, parents, g_scores, f_scores
            )

    def h_cost(self, current_node):
        return current_node.distance(self.nodes[self.end_id])

    def minimum(self, opened, f_scores):
        min_id = None
        min_f_score = math.inf
        for identifier in opened:
            f_score = f_scores.get(identifier, math.inf)
            if (f_score < min_f_score):
                min_id = identifier
                min_f_score = f_score
        return min_id

    def explore(self, min_id, closed, opened, parents, g_scores, f_scores):
        min_node = self.nodes[min_id]
        for neighbor_id in min_node.routes:
            if neighbor_id not in closed:
                if neighbor_id not in opened:
                    opened.add(neighbor_id)
                node = self.nodes[neighbor_id]
                g_score = g_scores.get(min_id, math.inf)
                g_score += min_node.distance(node)
                if g_score < g_scores.get(neighbor_id, math.inf):
                    parents[neighbor_id] = min_id
                    g_scores[neighbor_id] = g_score
                    h_score = self.h_cost(node)
                    f_scores[neighbor_id] = g_score + h_score

    def solve(self):
        if self.start_id == self.end_id:
            print(self.nodes[self.start_id].full_name)
            exit()

        parents = self.search()
        current_id = self.end_id
        stack = []

        if parents is None:
            print("IMPOSSIBLE")
            exit()

        while current_id in parents:
            stack.append(current_id)
            current_id = parents[current_id]
        stack.append(current_id)
        while len(stack) != 0:
            print(self.nodes[stack.pop()].full_name)


graph = Graph()
graph.read_game_input()
graph.solve()
