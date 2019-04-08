links = []
gateways = []


def sever(link):
    print("{} {}".format(link[0], link[1]))


def block(agent_node):
    for gateway in gateways:
        # Check for a direct link between the agent and a gateway
        for index, link in enumerate(links):
            if link == (agent_node, gateway) or link == (gateway, agent_node):
                sever(link)
                del links[index]
                return
    block_first_link()


def block_first_link():
    sever(links[0])
    del links[0]


nb_nodes, nb_links, nb_exits = [int(i) for i in input().split()]
for i in range(nb_links):
    link = tuple([int(j) for j in input().split()])
    links.append(link)

for i in range(nb_exits):
    gateway = int(input())
    gateways.append(gateway)

# game loop
while True:
    agent_node = int(input())
    block(agent_node)
