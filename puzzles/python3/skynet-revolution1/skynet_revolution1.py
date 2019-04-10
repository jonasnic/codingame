from collections import deque


def bfs(graph, gateways, agent_node_id):
    visited = set()
    queue = deque()
    came_from = {}  # node_id => parent node id on the shortest path
    queue.append(agent_node_id)
    visited.add(agent_node_id)

    while len(queue) != 0:
        node_id = queue.popleft()
        for neighbor_id in graph[node_id]:
            if neighbor_id not in visited:
                visited.add(neighbor_id)
                queue.append(neighbor_id)
                came_from[neighbor_id] = node_id
                if neighbor_id in gateways:
                    return (came_from, neighbor_id)


def reconstruct_path(graph, came_from, neighbor_id):
    current_id = neighbor_id
    stack = []

    while current_id in came_from:
        stack.append(current_id)
        current_id = came_from[current_id]
    stack.append(current_id)
    return stack


# read game input
graph = {}  # node_id => links set
gateways = set()
nb_nodes, nb_links, nb_gateways = map(int, input().split())
for i in range(nb_links):
    # n1 and n2 defines a link between these nodes
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = set()
    if n2 not in graph:
        graph[n2] = set()
    graph[n1].add(n2)
    graph[n2].add(n1)
for i in range(nb_gateways):
    gateways.add(int(input()))

# game loop
while True:
    agent_node_id = int(input())  # node id on which the Skynet agent is located
    came_from, neighbor_id = bfs(graph, gateways, agent_node_id)
    path = reconstruct_path(graph, came_from, neighbor_id)
    second_node_id = path[-2]
    graph[agent_node_id].remove(second_node_id)
    graph[second_node_id].remove(agent_node_id)
    # the indices of the nodes you wish to sever the link between
    print("{} {}".format(agent_node_id, second_node_id))
