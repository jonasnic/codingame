class Node:
    def __init__(self, digit):
        self.digit = digit
        self.children = []

    def index(self, digit):
        for i, child in enumerate(self.children):
            if child.digit == digit:
                return i
        return -1

    def add_child(self, digit):
        child = Node(digit)
        self.children.append(child)


nb_phones = int(input())
nb_nodes = 0
root = Node(-1)

for i in range(nb_phones):
    telephone = input()
    current = root
    for char in telephone:
        digit = int(char)
        i = current.index(digit)
        if (i == -1):
            current.add_child(digit)
            nb_nodes += 1
            i = current.index(digit)
        current = current.children[i]

print(nb_nodes)
